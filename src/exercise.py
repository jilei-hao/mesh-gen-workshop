import image_helpers as ih
import mesh_helpers as mh
import commons
import os

DIR_OUTPUT = commons.getOutputDirectory()

# Exercise 1: Get a list of unique labels from a image (including background)
def getUniqueLabels(image):
  """
  Args:
    image (SimpleITK.Image): Input multi-label image
  Output:
    list: List of unique labels in the image
  """
  # get unique labels in the image
  unique_labels = ih.getPixels(image)
  unique_labels = unique_labels.flatten()
  unique_labels = list(set(unique_labels))
  return unique_labels



# Exercise 2: Merge specified labels in the input image to the newLabel
# - Output: A new binary image with merged label as 1, everything else as 0
def mergeLabel(image, labelsToMerge):
  """
  Args:
    image (SimpleITK.Image): Input image
    labelsToMerge (list): List of labels to merge
  Output:
    SimpleITK.Image: Binary image with merged labels as 1 and everything else as 0
  """
  # merge the labels in the image based on the list
  labelImages = []
  for label in labelsToMerge:
    labelImages.append(ih.threshold(image, label, label, 1, 0))
  
  # add all label images up
  merged_image = labelImages[0]
  for i in range(1, len(labelImages)):
    merged_image = ih.addImages(merged_image, labelImages[i])

  # threshold the merged image
  merged_image = ih.threshold(merged_image, 1, 1, 1, 0)
  return merged_image



# Exercise 3: Create Creaseless Leaflets Models
def createCreaselessLeaflets(image, leafletLabel, rootLabel):
  """
  Args:
    image (SimpleITK.Image): Input multi-label image
    leafletLabel (int): Label for leaflets
    rootLabel (int): Label for root
  Output:
    vtkPolyData: Mesh for the merged leaflets
  """

  # merge the leaflets
  leafletImage = mergeLabel(image, [leafletLabel, rootLabel])

  # get a vtkImageData from the leaflet image
  leafletVTK = ih.sitkToVtk(leafletImage)

  # get the mesh from the vtkImageData
  leafletMesh = mh.getMeshFromVTKImage(leafletVTK)

  return leafletMesh


# Exercise 4: Create a Multilabel Pipeline
def createMultiLabelCreaselessMesh(image, leafletLabels, rootLabel):
  """
  Args:
    image (SimpleITK.Image): Input multi-label image
    leafletLabels (list): List of labels for leaflets
    rootLabel (int): Label for root
  Output:
    vtkPolyData: a multilabel mesh with creaseless leaflets
  """
  # create a list of meshes for each leaflet
  meshes = []
  for leafletLabel in leafletLabels:
    meshes.append(createCreaselessLeaflets(image, leafletLabel, rootLabel))

  # append all the meshes
  appendedMesh = mh.appendMeshes(meshes)
  return appendedMesh


# Exercise 4 Bonus: Create a Multilabel Pipeline with fused leaflets
def createMultiLabelCreaselessMeshFused(image, leafletLabelsGroup, rootLabel):
  """
  Args:
    image (SimpleITK.Image): Input multi-label image
    leafletLabels (list): List of Group of labels for leaflets e.g. [[1], [2, 3]]
    rootLabel (int): Label for root
  Output:
    vtkPolyData: a multilabel mesh with creaseless leaflets
  """
  # merge leaflets in each group
  mergedLeaflets = []

  for leafletLabels in leafletLabelsGroup:
    mergedLeaflets.append(mergeLabel(image, leafletLabels))

  rootImage = ih.threshold(image, rootLabel, rootLabel, 1, 0)

  # merge merged leaflets and root
  meshes = []
  for mergedLeaflet in mergedLeaflets:
    # note that createCreaselessLeaflets creates wrong result, why?
    withRoot = ih.addImages(mergedLeaflet, rootImage)
    meshes.append(mh.getMeshFromVTKImage(ih.sitkToVtk(withRoot)))

  # append all the meshes
  appendedMesh = mh.appendMeshes(meshes)
  return appendedMesh