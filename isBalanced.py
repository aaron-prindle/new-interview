class BSTNode:
  def __init__(self,key,left=None,right=None):
    self.key = key
    self.left = left
    self.right = right

def isBalanced(root):
  if isBalRecurse(root) == -1:
    return False
  return True

def isBalRecurse(root):
  if root == None:
    return 0
  leftH = isBalRecurse(root.left)
  if leftH == -1:
    return -1
  rightH = isBalRecurse(root.right)
  if rightH == -1:
    return -1
  diff = abs(leftH-rightH)
  if diff>1:
    return -1
  return max(leftH,rightH)+1

def main():
  five = BSTNode(5)
  four = BSTNode(4)
  three = BSTNode(3,four,five)
  two = BSTNode(2,None,None)
  one = BSTNode(1,two,three)
  print isBalanced(one)

main()
