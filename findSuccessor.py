class BSTNode:
  def __init__(self,key=None,left=None,right=None,parent=None):
    self.key = key
    self.left = left
    self.right = right
    self.parent = parent

def findSuccessor(n):
  if n.right:
    cur = n.right
    while cur.left:
      cur = cur.left
    return cur
  elif n.parent.left == n:
    return n.parent
  elif n.parent.right == n:
    cur = n.parent
    if cur.parent == None:
      return None
    while(cur.parent.left!=cur):
      if cur.parent==None:
        return None
      cur=cur.parent
    return cur
  return None

def main():
  three = BSTNode(3,None,None,None)
  one = BSTNode(1,None,None,None)
  two = BSTNode(2,one,three,None)
  three.parent = two
  one.parent = two
  successor = findSuccessor(one)
  if successor:
    print successor.key
  else:
    print successor
main()
