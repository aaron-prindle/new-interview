class TreeNode:
  def __init__(self,val,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

def isBalanced(root):
  if getHeight(root) == -1:
    return False
  return True
      
def getHeight(root):
  if not root:
    return 0
  leftH = getHeight(root.left)
  if leftH == -1:
    return -1
  rightH = getHeight(root.right)
  if rightH == -1:
    return -1
  diff = abs(leftH-rightH)
  if diff > 1:
    return -1
  return max(leftH,rightH)+1
        
def main():
  three = TreeNode(3)
  two = TreeNode(2,three)
  one = TreeNode(1,two)
  print isBalanced(one)

main()
