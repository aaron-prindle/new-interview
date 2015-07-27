class BNode:
  def __init__(self,key=None,left=None,right=None, parent=None):
    self.key = key
    self.left = left
    self.right = right
    self.parent = parent

def bstCheck(n):
  print n.key
  if n == None:
    return True
  if n.left:
    if n.left.key<=n.key:
      out = bstCheck(n.left)
      if out == False:
        return False
    else:
      return False
  if n.right:
    if n.right.key>n.key:
      out = bstCheck(n.right)
      if out == False:
        return False
    else:
      return False
  return True

def main():
  three = BNode(3,None,None)
  one = BNode(1,None,None)
  two = BNode(2,one,three)
  print bstCheck(one)

main()
