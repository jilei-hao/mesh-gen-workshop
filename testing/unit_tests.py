import sys
import os
import test_helpers as th
import SimpleITK as sitk

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import image_helpers as ih
import exercise as ex

def test_e1_t1(data):
  # Test case 1: Get Unique Labels
  result = ex.getUniqueLabels(data["image"])

  # Check if the output is a list
  if (type(result) != list):
    th.printFailingMessage("Test case 1 failed: Output is not a list")
    return False
  
  # Check if the output is a list of unique labels
  unique_labels = set(result)
  if (len(unique_labels) != len(result)):
    th.printFailingMessage("Test case 1 failed: Output list contains duplicate labels")
    return False
  
  # Check if the label values are correct
  expected_labels = [0, 1, 2, 3, 4, 5, 6]
  if (unique_labels != set(expected_labels)):
    th.printFailingMessage("Test case 1 failed: Output list does not match expected labels")
    return False
  
  th.printPassingMessage("Test case 1 passed: Unique labels are correct")


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
  # Check if the label values are correct
  if (result != uniqueLabels):
    th.printFailingMessage("Test case 2 failed: Output list does not match expected labels")
    return False
  
  th.printPassingMessage("Test case 2 passed: Unique labels are correct")


def test_e2_t1(data):
  return None


def main():
  testData = {}

  dataFolder = os.path.join(os.path.dirname(__file__), '..', 'data')
  testData["image"] = ih.readImage("srd.nii.gz")

  test_e1_t1(testData)
  test_e1_t2(testData)
  test_e2_t1(testData)
  print("\n\n")


if __name__ == "__main__":
  main()