# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
      return self.getHeight(root)
    def getHeight(self,root):
      if not root:
        return 0
      leftH = self.getHeight(root.left)
      rightH = self.getHeight(root.right)
      return max(leftH,rightH)+1
    

def main():
  solution = Solution()
  five = TreeNode(5)
  four = TreeNode(4)
  three = TreeNode(3)
  two = TreeNode(2,three,four)
  one = TreeNode(1,two,five)
  print solution.maxDepth(one)

main()
