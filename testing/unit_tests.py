import sys
import os
import test_helpers as th
import SimpleITK as sitk
import vtk

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import image_helpers as ih
import mesh_helpers as mh
import exercise as ex
import commons

DATA_DIR = commons.getDataDirectory()
OUTPUT_DIR = commons.getOutputDirectory()

def test_e1_t1(data):
  # test_e1_t1: Get Unique Labels
  result = ex.getUniqueLabels(data["image"])

  # Check if the output is a list
  if (type(result) != list):
    th.printFailingMessage("test_e1_t1 failed: Output is not a list")
    return False
  
  # Check if the output is a list of unique labels
  unique_labels = set(result)
  if (len(unique_labels) != len(result)):
    th.printFailingMessage("test_e1_t1 failed: Output list contains duplicate labels")
    return False
  
  # Check if the label values are correct
  expected_labels = [0, 1, 2, 3, 4, 5, 6]
  if (unique_labels != set(expected_labels)):
    th.printFailingMessage("test_e1_t1 failed: Output list does not match expected labels")
    return False
  
  th.printPassingMessage("test_e1_t1 passed: Unique labels are correct")


def test_e1_t2(data):
  uniqueLabels = [0, 23, 54, 73, 222, 238]

  # Make a dummy simpleITK image with label values in the unique labels list
  image = sitk.Image(10, 10, 10, sitk.sitkUInt16)

  size = image.GetSize()
  for z in range(size[2]):
    for y in range(size[1]):
      for x in range(size[0]):
        index = (x, y, z)
        image.SetPixel(index, uniqueLabels[(x + y + z) % len(uniqueLabels)])

  result = ex.getUniqueLabels(image)

  if (not result or result.__len__() == 0):
    th.printFailingMessage("test_e1_t2 failed: Output is empty")
    return False
      
  # sort the result
  result.sort()

  # Check if the label values are correct
  if (result != uniqueLabels):
    th.printFailingMessage("test_e1_t2 failed: Output list does not match expected labels")
    th.printFailingMessage(f"-- Expected: {uniqueLabels}")
    th.printFailingMessage(f"-- Got: {result}")
    return False
  
  th.printPassingMessage("test_e1_t2 passed: Unique labels are correct")


def test_e2_t1(data):
  mergedLabels = [1, 2, 3, 4, 5, 6]
  result = ex.mergeLabel(data["image"], mergedLabels)

  # Check if the output is a SimpleITK image
  if (type(result) != sitk.Image):
    th.printFailingMessage("test_e2_t1 failed: Output is not a SimpleITK image")
    return False
  
  # Check if output is a binary image
  if (len(ex.getUniqueLabels(result)) != 2):
    th.printFailingMessage("test_e2_t1 failed: Output is not a binary image")
    return False
  
  # write out one-label image
  ih.writeImage(result, os.path.join(OUTPUT_DIR, 'e2_all-labels.nii.gz'))
  
  th.printPassingMessage("test_e2_t1 passed: Merged labels are correct")


def test_e3_t1(data):
  result1 = ex.createCreaselessLeaflets(data["image"], 1, 4)

  # Check if the output is a vtkPolyData
  if (type(result1) != vtk.vtkPolyData):
    th.printFailingMessage("test_e3_t1 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result1.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e3_t1 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result1, os.path.join(OUTPUT_DIR, 'e3_leaflet_1.vtp'))

  th.printPassingMessage("test_e3_t1 passed: Creaseless Mesh for leaflet 1 is correct")

def test_e3_t2(data):
  result2 = ex.createCreaselessLeaflets(data["image"], 2, 4)

  # Check if the output is a vtkPolyData
  if (type(result2) != vtk.vtkPolyData):
    th.printFailingMessage("test_e3_t2 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result2.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e3_t2 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result2, os.path.join(OUTPUT_DIR, 'e3_leaflet_2.vtp'))

  th.printPassingMessage("test_e3_t2 passed: Creaseless Mesh for leaflet 2 is correct")


def test_e3_t3(data):
  result3 = ex.createCreaselessLeaflets(data["image"], 3, 4)

  # Check if the output is a vtkPolyData
  if (type(result3) != vtk.vtkPolyData):
    th.printFailingMessage("test_e3_t3 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result3.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e3_t3 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result3, os.path.join(OUTPUT_DIR, 'e3_leaflet_3.vtp'))

  th.printPassingMessage("test_e3_t3 passed: Creaseless Mesh for leaflet 3 is correct")


def test_e4_t1(data):
  result = ex.createMultiLabelCreaselessMesh(data["image"], [1, 2, 3], 4)

  # Check if the output is a vtkPolyData
  if (type(result) != vtk.vtkPolyData):
    th.printFailingMessage("test_e4_t1 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e4_t1 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result, os.path.join(OUTPUT_DIR, 'e4_multi-label.vtp'))

  th.printPassingMessage("test_e4_t1 passed: Creaseless Mesh for leaflets is correct")


def test_e4_t2(data):
  result = ex.createMultiLabelCreaselessMeshFused(data["image"], [[1, 2], [3]], 4)

  # Check if the output is a vtkPolyData
  if (type(result) != vtk.vtkPolyData):
    th.printFailingMessage("test_e4_t2 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e4_t2 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result, os.path.join(OUTPUT_DIR, 'e4_multi-label-1-2-fused.vtp'))

  th.printPassingMessage("test_e4_t2 passed: Creaseless Mesh for leaflets is correct")

def test_e4_t3(data):
  result = ex.createMultiLabelCreaselessMeshFused(data["image"], [[1], [2, 3]], 4)

  # Check if the output is a vtkPolyData
  if (type(result) != vtk.vtkPolyData):
    th.printFailingMessage("test_e4_t3 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e4_t3 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result, os.path.join(OUTPUT_DIR, 'e4_multi-label-2-3-fused.vtp'))

  th.printPassingMessage("test_e4_t3 passed: Creaseless Mesh for leaflets is correct")


def test_e4_t4(data):
  result = ex.createMultiLabelCreaselessMeshFused(data["image"], [[2], [1, 3]], 4)

  # Check if the output is a vtkPolyData
  if (type(result) != vtk.vtkPolyData):
    th.printFailingMessage("test_e4_t4 failed: Output is not a vtkPolyData")
    return False
  
  # Check if the output has points
  if (result.GetNumberOfPoints() == 0):
    th.printFailingMessage("test_e4_t4 failed: Output has no points")
    return False
  
  # write out the mesh
  mh.writeMesh(result, os.path.join(OUTPUT_DIR, 'e4_multi-label-1-3-fused.vtp'))
  
  th.printPassingMessage("test_e4_t4 passed: Creaseless Mesh for leaflets is correct")


def main():
  testData = {}
  testData["image"] = ih.readImage(os.path.join(DATA_DIR, 'srd.nii.gz'))

  # create the output folder if not exists
  if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


  test_e1_t1(testData)
  test_e1_t2(testData)
  test_e2_t1(testData)
  test_e3_t1(testData)
  test_e3_t2(testData)
  test_e3_t3(testData)
  test_e4_t1(testData)
  test_e4_t2(testData)
  test_e4_t3(testData)
  test_e4_t4(testData)
  
  print("\n\n")


if __name__ == "__main__":
  main()