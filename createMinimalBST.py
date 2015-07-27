class TreeNode:
  def __init__(self,key=None,left=None,right=None):
    self.key = key
    self.left = left
    self.right = right

def createMinimalBSTRecurse(a, s, e):
  if e < s:
    return None
  mid = (s+e)/2
  n = TreeNode(a[mid])
  n.left = createMinimalBSTRecurse(a,s,mid-1)
  n.right = createMinimalBSTRecurse(a,mid+1,e)
  return n
  
def createMinimalBST(a):
  return createMinimalBSTRecurse(a,0,len(a)-1)

def inOrder(n):
  if n.left:
    inOrder(n.left)
  print n.key
  if n.right:
    inOrder(n.right)
  

def main():
  a = range(1,10)
  n = createMinimalBST(a)
  inOrder(n)

main()
