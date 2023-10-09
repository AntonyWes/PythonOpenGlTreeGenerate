from yaml import load, FullLoader

from OpenGLLogic import TreeViewer
from Tree import Tree

with open('data.yaml') as fh:
    read_data = load(fh, Loader=FullLoader)

TreeObj = Tree(**read_data)
tree_list = [[] for i in range(10)]
for item in TreeObj.get_elements(0):
    tree_list[item[0]].append(item[1])
print(tree_list)
# Tree = TreeViewer(TreeObj, 900, 800, tree_list)
# Tree.show()
