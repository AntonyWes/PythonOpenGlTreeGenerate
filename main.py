from yaml import load, FullLoader

from OpenGLLogic import TreeViewer
from Tree import Tree

with open('data.yaml') as fh:
    read_data = load(fh, Loader=FullLoader)

TreeObj = Tree(**read_data)
Tree = TreeViewer(TreeObj, 900, 800)
Tree.show()
