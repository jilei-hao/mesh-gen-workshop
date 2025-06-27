import image_helpers as ih
import mesh_helpers as mh
import vtk
import sys


def main():
  # get image filename from command line argument

  if len(sys.argv) < 3:
    print("Usage: python demo_orientation.py image.nii.gz output.vtk")
    return
  
  fn_image = sys.argv[1]
  fn_output = sys.argv[2]

  # read image
  image = ih.readImage(fn_image)

  # print image meta
  print("Image Size:", image.GetSize())
  print("Image Origin:", image.GetOrigin())
  print("Image Spacing:", image.GetSpacing())
  print("Image Direction:", image.GetDirection())

  # threshold the image to binary
  binary_image = ih.threshold(image, 1, 100, 1, 0)


  # convert to vtkImageData
  vtk_image = ih.sitkToVtk(binary_image)

  # print vtkImageData meta
  print("VTK Image Size:", vtk_image.GetDimensions())
  print("VTK Image Origin:", vtk_image.GetOrigin())
  print("VTK Image Spacing:", vtk_image.GetSpacing())
  print("VTK Image Direction:", vtk_image.GetDirectionMatrix())


  # get mesh from vtkImageData
  mesh = mh.getMeshFromVTKImage(vtk_image)

  # flip the LR, AP directions
  # this is necessary to match the orientation of the mesh with the image
  flip_matrix = vtk.vtkMatrix4x4()
  flip_matrix.Identity()
  flip_matrix.SetElement(0, 0, -1)  # flip X direction
  flip_matrix.SetElement(1, 1, -1)  # flip Y direction
  flip_matrix.SetElement(2, 2, 1)   # keep Z direction

  vtk_transform = vtk.vtkTransform()
  vtk_transform.SetMatrix(flip_matrix)
  vtk_transform_filter = vtk.vtkTransformPolyDataFilter()
  vtk_transform_filter.SetTransform(vtk_transform)
  vtk_transform_filter.SetInputData(mesh)
  vtk_transform_filter.Update()
  mesh = vtk_transform_filter.GetOutput()




  # write mesh to file
  mh.writeMesh(mesh, fn_output)


if __name__ == "__main__":
  main()
  
