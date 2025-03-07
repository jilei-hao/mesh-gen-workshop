import os
import sys
import SimpleITK as sitk
import image_helpers as ih
import mesh_helpers as mh
import exercise as ex

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')

def main():
  image = ih.readImage(os.path.join(DATA_DIR, 'srd.nii.gz'))
  bImage = ih.threshold(image, 1, 100, 1, 0)
  ih.writeImage(bImage, os.path.join(DATA_DIR, 'binary.nii.gz'))
  
  bImageVTK = ih.sitkToVtk(bImage)

  mesh = mh.getMeshFromVTKImage(bImageVTK)

  mh.writeMesh(mesh, os.path.join(DATA_DIR, 'mesh.vtp'))

  
if __name__ == "__main__":
  main()

