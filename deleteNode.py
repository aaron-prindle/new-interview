# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
      if not node:
        return None
      node.val = node.next.val
      node.next = node.next.next
      return

def main():

main()
