import SimpleITK as sitk
from picsl_c3d import Convert3D
import vtk

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
  return 1

# get Pixels in a SimpleITK image
def getPixels(image):
  pixels = sitk.GetArrayFromImage(image)
  return pixels




# threshold a SimpleITK image
def threshold(image, lower, upper, valueIn, valueOut):
  return 1


# convert a SimpleITK image to a vtkImageData
def sitkToVtk(image):
  return 1


# smooth a vtkImageData
def smoothVTKImage(image, sigma):
  return 1