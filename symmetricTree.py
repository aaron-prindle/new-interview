from sys import maxint

#1,2,3,3,null,2,null
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x,left=None,right=None):
    self.val = x
    self.left = left
    self.right = right
    
class Solution:
  # @param {TreeNode} root
  # @return {boolean}
  def isSymmetric(self, root):
    if not root or (not root.left and not root.right):
      return True
    if root.left and root.right:
      left = self.bfs(root.left)
      right = self.bfs(root.right)
      while(True):
        l = left.next()
        r = right.next()
        print l,r
        if l != r[::-1]:
          return False
        if l == []:
          break
      return True
    return False
    
  def bfs(self,u):
    seen = set()
    seen.add(u)
    frontier = [u]
    out = [u]
    while frontier:
      yield [i.val for i in out]
      nxt = []
      out = []
      for u in frontier:
        if u.left:
          nxt.append(u.left)
          out.append(u.left)
        else:
          out.append(TreeNode(-maxint))
        if u.right:
          nxt.append(u.right)
          out.append(u.right)
        else:
          out.append(TreeNode(-maxint))
      frontier = nxt
    yield []

def main():
  # threeR = TreeNode(3)
  # threeL = TreeNode(3)
  # twoL = TreeNode(2,threeL,None)
  # twoR = TreeNode(2,threeR,None)
  # one = TreeNode(1,twoL,twoR)
  twoL = TreeNode(2,None,None)
  twoR = TreeNode(2,None,None)
  one = TreeNode(1,twoL,twoR)
  
  solution = Solution()
  print solution.isSymmetric(one)

main()
        
