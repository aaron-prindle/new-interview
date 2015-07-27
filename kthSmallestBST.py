# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
      cur = [0]
      inOrder(root,cur)
      return cur[0]
      
    def inOrder(self,root,cur):
      if root == None:
        return None
      inOrder(root.left)
      cur[0] += 1
      inOrder(root.right)
  
def main():

main()
