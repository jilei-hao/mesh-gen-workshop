import SimpleITK as sitk
import picsl_c3d as c3d
import vtk

# read an image file from disk and return a SimpleITK image
def readImage(filename):
  return 1


# write a SimpleITK image to disk
def writeImage(image, filename):
  return 1


# threshold a SimpleITK image
def threshold(image, lower, upper, valueIn, valueOut):
  return 1


# convert a SimpleITK image to a vtkImageData
def sitkToVtk(image):
  return 1


# smooth a vtkImageData
def smoothVTKImage(image, sigma):
  return 1