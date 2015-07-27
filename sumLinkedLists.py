class Node:
  def __init__(self,key=None,nxt=None):
    self.key = key
    self.nxt = nxt

def sumLinkedLists(l1,l2):
  summ = 0
  carry = 0
  out = None
  while l1 or l2 or carry:
    summ = 0
    if l1:
      summ += l1.key
      l1 = l1.nxt
    if l2:
      summ += l2.key
      l2 = l2.nxt
    summ += carry
    if summ >=10:
      summ -= 10
      carry = 1
    else:
      carry = 0
    new = Node(summ)
    if out:
      out.nxt = new
      out = new
    else:
      out = new
      head = new
  return head

def main():
  one = Node(1,None)
  two = Node(2,one)
  three = Node(8,two)

  two2 = Node(2,None)
  three2 = Node(3,two2)

  head = sumLinkedLists(three,three2)
  while(head):
    print head.key
    head = head.nxt

  print "========================================"

  nine = Node(9,None)
  nine2 = Node(9,None)

  head = sumLinkedLists(nine,nine2)
  while(head):
    print head.key
    head = head.nxt


main()
