import xml.etree.ElementTree as xeet
import os

file = os.path.join('.', 'aemet.xml')
def readXml(file):
    tree = xeet.parse(file)
    root = tree.getroot()
    return root

root, tree = readXml(file)
print(tree)