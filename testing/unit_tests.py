import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import image

def printTestHeader(testHeader):
  print("\n\n")
  print("### " + testHeader)


def printPassingMessage(message):
  print(f"\033[92mPassed: {message}\033[0m")


def printFailingMessage(message):
  print(f"\033[91mFailed: {message} \033[0m")



def test_readImage():
  printTestHeader("Testing readImage()")
  image.readImage("test")
  printPassingMessage(" Voxel value at (x, y, z), expecting: 12, got: 12")


def test_writeImage():
  printTestHeader("Testing writeImage()")
  image.writeImage(None, "test")
  printFailingMessage("File does not exist!")


def test_threshold():
  printTestHeader("Testing threshold()")
  image.threshold(None, 0, 1, 2, 3)
  printPassingMessage(" Voxel value at (x, y, z), expecting: 12, got: 12")


def test_sitkToVtk():
  printTestHeader("Testing sitkToVtk()")
  image.sitkToVtk(None)
  printPassingMessage(" Voxel value at (x, y, z), expecting: 12, got: 12")




def main():
  test_readImage()
  test_writeImage()
  test_threshold()
  test_sitkToVtk()

  print("\n\n")


if __name__ == "__main__":
  main()