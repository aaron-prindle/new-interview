# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.invertRecurse(root)
        return root
    def invertRecurse(self,n):
      if not n:
        return
      tmp = n.left
      n.left = n.right
      n.right = tmp
      self.invertRecurse(n.left)
      self.invertRecurse(n.right)
