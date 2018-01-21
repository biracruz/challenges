""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBSTAux(node, _min, _max):
    if node is None:
        return True
    
    if node.data < _min or node.data > _max:
        return False
    
    return checkBSTAux(node.left, _min, node.data -1) and checkBSTAux(node.right, node.data + 1, _max)
        
    
def checkBST(root):
    return checkBSTAux(root, -4294967296, 4294967296)