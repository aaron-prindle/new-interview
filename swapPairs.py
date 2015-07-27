class ListNode:
  def __init__(self,x, nxt=None):
    self.val = x
    self.nxt = nxt

    def swap(n1,n2):
      n1.next = n2.next
      n2.next = n1
    
    def swapPairs(head):
      if head == None or head.next == None:
        return head
      p1 = head
      p2 = head.next
      oldP = None
      if not head.next.next:
        p1.next = None
        p2.next = p1
        return p2
      flag = True
      while(p1.next):
        swap(p1,p2)
        if oldP:
          oldP.next = p2
        if flag:
          head = p2
          flag = False
        if p1.next and p1.next.next:
          oldP = p1
          p2 = p1.next.next
          p1 = p1.next
        else:
          break
      return head

def main():
  four = ListNode(4,None)
  three = ListNode(3,four)
  two = ListNode(2,three)
  one = ListNode(1,two)
  head = swapPairs(one)
  while(head):
    print head.val
    head = head.nxt
main()
