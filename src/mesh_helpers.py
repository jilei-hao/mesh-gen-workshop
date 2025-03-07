import vtk

def getMeshFromVTKImage(image):
  # Create a marching cubes object
  mc = vtk.vtkMarchingCubes()
  
  # Set the input image
  mc.SetInputData(image)
  
  # Set the contour value
  mc.SetValue(0, 1)
  
  # Update the marching cubes
  mc.Update()
  
  # Get the output
  mesh = mc.GetOutput()
  
  return mesh

def appendMeshes(meshes):
  # Create a vtkAppendPolyData object
  append = vtk.vtkAppendPolyData()
  
  # Add all the meshes to the vtkAppendPolyData object
  for mesh in meshes:
    append.AddInputData(mesh)
  
  # Update the append object
  append.Update()
  
  # Get the appended mesh
  appendedMesh = append.GetOutput()
  
  return appendedMesh

def writeMesh(mesh, filename):
  # write mesh based on the file extension
  if filename.endswith('.stl'):
    writer = vtk.vtkSTLWriter()
  elif filename.endswith('.ply'):
    writer = vtk.vtkPLYWriter()
  elif filename.endswith('.vtk'):
    writer = vtk.vtkPolyDataWriter()
  elif filename.endswith('.vtp'):
    writer = vtk.vtkXMLPolyDataWriter()
  else:
    raise ValueError(f"Unsupported file format: {filename}")
  
  # Set the input mesh
  writer.SetInputData(mesh)
  writer.SetFileName(filename)
  writer.Write()

  