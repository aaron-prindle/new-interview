# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
      if not head:
        return head
      self.mergesort(head)

    def getListLen(self,head):
      length =1
      while head:
        length+=1
        head=head.next
      return length
    
    def halfWayNodeAndBreakLL(self,head,length):
      for i in xrange(length/2):
        head=head.next
      halfHead = head.next
      head.next = None
      print halfHead.val
      return halfHead

    def mergesort(self,head):
      merged = None
      #getLen of piece
      length = self.getListLen(head)
      print length
      if length > 1:
        #store rHead
        #break @ len/2
        rHead = self.halfWayNodeAndBreakLL(head,length)
        #curhead = lHead
        lHead = head
        #self.mergesort(lHead)
        #self.mergesort(rHead)
        merged = self.merge(lHead,rHead)
      return merged

    def addToHead(self,head,node):
      if head == None:
        head = node
      else:
        node.next = head
        head = node

    def merge(self,lHead,rHead):
      head = None
      headP = None
      while lHead or rHead:
        if not lHead:
          nextRHead = rHead.next
          if headP == None:
            head = rHead
            headP = rHead
          else:
            rHead.next = headP
            headP = rHead
          rHead = nextRHead
        elif not rHead:
          nextLHead = lHead.next
          if headP == None:
            head = lHead
            headP = lHead
          else:
            lHead.next = headP
            headP = lHead
          lHead = nextLHead
        else:
          if lHead.val <= rHead.val:
            nextLHead = lHead.next
            if headP == None:
              head = lHead
              headP = lHead
            else:
              lHead.next = headP
              headP = lHead
            lHead = nextLHead
          else:
            nextRHead = rHead.next
            if headP == None:
              head = rHead
              headP = rHead
            else:
              rHead.next = headP
              headP = rHead
            rHead = nextRHead

def main():
  six  = ListNode(6)
  five = ListNode(5)
  four = ListNode(4)
  three = ListNode(3)
  two = ListNode(2)
  one = ListNode(1)
  six.next = five
  five.next = four
  four.next = three
  three.next = two
  two.next = one
  solution = Solution()

  print solution.sortList(six)
  
main()
