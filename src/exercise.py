import image_helpers as ih
import mesh_helpers as mh
import commons

# Exercise 1: Get a list of unique labels from a image (including background)
def getUniqueLabels(image):
  """
  Args:
    image (SimpleITK.Image): Input multi-label image
  Output:
    list: List of unique labels in the image
  """
  pass



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
  pass


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

  pass


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
  pass


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
  pass