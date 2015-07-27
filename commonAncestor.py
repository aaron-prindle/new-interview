class TreeNode:
  def __init__(self,key=None,left=None,right=None):
    self.key = key
    self.left = left
    self.right = right

def covers (root, p):
  if root == None:
    return False
  if root == p:
    return True
  return covers(root.left,p) or covers(root.right, p)

def commonAncestorHelper(root,p,q):
  if root == None:
    return None
  if root == p or root == q:
    return q
  
  is_p_on_left = covers(root.left,p)
  is_q_on_left = covers(root.left,q)

  if (is_p_on_left != is_q_on_left):
    return root
  child_side =  root.left if is_p_on_left else root.right
  return commonAncestorHelper(child_side,p,q)
  
def commonAncestor(root,p,q):
  if (not covers(root,p) or not covers(root,q)):
      return None
  return commonAncestorHelper(root,p,q)

def main():
  three = TreeNode(3,None,None)
  one = TreeNode(1,None,None)
  two = TreeNode(2,one,three)
  print commonAncestor(two,one,three).key

main()
