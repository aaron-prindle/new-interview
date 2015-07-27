class TreeNode:
  def __init__(self,key,left,right):
    self.key = key
    self.left = left
    self.right = right

def containsTree(t1,t2):
  if t2 == None:
    return True
  return subTree(t1,t2)

def subTree(r1,r2):
  if r1 == None:
    return False
  if r1.key == r2.key:
    if(matchTree(r1,r2)):
      return True
  return subTree(r1.left,r2) || subTree(r1.right,r2)
  
def matchTree(r1,r2):
  if r2 == None and r1 == None:
    return True

  if r1 == None or r2 == None:
    return False

  if (r1.key != r2.key):
    return False

  return (matchTree(r1.left,r2.left) and mathTree(r1.right,r2.right))
