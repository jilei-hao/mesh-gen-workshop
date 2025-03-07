import os

def getSrcDirectory():
  return os.path.dirname(os.path.realpath(__file__))

def getDataDirectory():
  return os.path.join(getSrcDirectory(), '..', 'data')

def getOutputDirectory():
  return os.path.join(getSrcDirectory(), '..', 'output')




