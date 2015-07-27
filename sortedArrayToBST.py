# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
      if not nums:
        return nums
      low = 0
      high = len(nums)-1
      mid = (low+high)/2
      root = TreeNode(nums[mid])
      root.left = self.binarySearch(nums,low,mid-1)
      root.right = self.binarySearch(nums,mid+1,high)
      return root
      
    def binarySearch(self,arr,low,high):
      mid = (low+high)/2
      if low>high:
        return
      node = TreeNode(arr[mid])
      node.left = self.binarySearch(arr,low,mid-1)
      node.right = self.binarySearch(arr,mid+1,high)
      return node

def printTree(root):
  if not root:
    return
  printTree(root.left)
  print root.val
  printTree(root.right)


def main():
  arr = [0,1,2,3,4,5,6]
  solution = Solution()
  root = solution.sortedArrayToBST(arr)
  printTree(root)

main()
