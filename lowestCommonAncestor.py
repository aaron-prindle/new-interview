# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

def inOrder(root,out):
  if not root:
    return
  inOrder(root.left,out)

  out.append(root)
  inOrder(root.right,out)
  
def postOrder(root,out):
  if not root:
    return
  postOrder(root.left,out)
  postOrder(root.right,out)
  out.append(root)

def lowestCommonAncestor(root, p, q):
  inorder = []
  inOrder(root,inorder)
  postorder = []
  postOrder(root,postorder)
  lIndex = inorder.index(p)
  hIndex = inorder.index(q)
  if p.val>q.val:
    tmp = lIndex
    lIndex = hIndex
    hIndex = tmp
  rangeSet = set()
  for i in range(lIndex,hIndex+1):
    rangeSet.add(inorder[i])
  last = None #iono
  for i in postorder:
    if i in rangeSet:
      last = i
      rangeSet.remove(i)
  return last


def main():
  one = TreeNode(1)
  two = TreeNode(2,one,None)
  print lowestCommonAncestor(two,two,one)
main()
