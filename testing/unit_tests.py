import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import image

def test_readImage():
  image.readImage("test")

def main():
  test_readImage()

if __name__ == "__main__":
  main()