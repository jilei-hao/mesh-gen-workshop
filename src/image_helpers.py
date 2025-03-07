import SimpleITK as sitk
import vtk
import numpy as np
from vtk.util.numpy_support import numpy_to_vtk

# read an image file from disk and return a SimpleITK image
def readImage(filename):
  # read the image using SimpleITK
  image = sitk.ReadImage(filename)
  # check if the image is valid
  if image is None:
    raise ValueError(f"Image {filename} is not valid")
  
  # check if the image is empty
  if image.GetSize() == (0, 0, 0):
    raise ValueError(f"Image {filename} is empty")
  
  return image


# write a SimpleITK image to disk
def writeImage(image, filename):
  # write the image using SimpleITK
  sitk.WriteImage(image, filename)


# get Pixels in a SimpleITK image
def getPixels(image):
  pixels = sitk.GetArrayFromImage(image)
  return pixels


# threshold a SimpleITK image
def threshold(image, lower, upper, valueIn, valueOut):
  # threshold the image using SimpleITK
  thresholded = sitk.BinaryThreshold(image, lower, upper, valueIn, valueOut)
  return thresholded


# add two SimpleITK images
def addImages(image1, image2):
  # add the images using SimpleITK
  added_image = sitk.Add(image1, image2)
  return added_image


# convert a SimpleITK image to a vtkImageData
def sitkToVtk(sitk_image):
  # Get the pixel data from SimpleITK as a numpy array
  pixel_data = sitk.GetArrayFromImage(sitk_image)
  
  # SimpleITK uses (x,y,z) ordering but VTK/NumPy use (z,y,x)
  # so we need to get the dimensions properly
  size = sitk_image.GetSize()
  
  # Create a VTK image data object
  vtk_image = vtk.vtkImageData()
  
  # Set the dimensions
  vtk_image.SetDimensions(size[0], size[1], size[2])
  
  # Set the origin - SimpleITK origin to VTK origin
  origin = sitk_image.GetOrigin()
  vtk_image.SetOrigin(origin[0], origin[1], origin[2])
  
  # Set the spacing - pixel size in each dimension
  spacing = sitk_image.GetSpacing()
  vtk_image.SetSpacing(spacing[0], spacing[1], spacing[2])
  
  # Create and populate the vtkImageData
  # Ensure we're using the right data type
  if pixel_data.dtype == np.uint8:
      vtk_array = numpy_to_vtk(pixel_data.ravel(), deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)
  elif pixel_data.dtype == np.int16:
      vtk_array = numpy_to_vtk(pixel_data.ravel(), deep=True, array_type=vtk.VTK_SHORT)
  elif pixel_data.dtype == np.uint16:
      vtk_array = numpy_to_vtk(pixel_data.ravel(), deep=True, array_type=vtk.VTK_UNSIGNED_SHORT)
  elif pixel_data.dtype == np.float32:
      vtk_array = numpy_to_vtk(pixel_data.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
  else:
      vtk_array = numpy_to_vtk(pixel_data.ravel(), deep=True)
  
  vtk_array.SetName("ImageScalars")
  vtk_image.GetPointData().SetScalars(vtk_array)
  
  return vtk_image



# smooth a vtkImageData
def smoothVTKImage(image, sigma):
  return 1