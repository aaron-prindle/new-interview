class ListNode:
  def __init__(self,val,nxt = None):
    self.val = val
    self.nxt = nxt

def setOrAdd(newP, newH, n):
  if not newP:
    newP = n
    newH = n
  else:
    newP.nxt = n
    newP = n
  return newP,newH

def mergeTwoLists(l1,l2):
  newP = None
  newH = None
  while l1 or l2:
    if not l1:
      newP, newH = setOrAdd(newP,newH,l2)
      l2 = l2.nxt
    elif not l2:
      newP, newH = setOrAdd(newP,newH,l1)
      l1 = l1.nxt
    else:
      if l1.val <= l2.val:
        newP, newH = setOrAdd(newP,newH,l1)
        l1 = l1.nxt
      else:
        newP, newH = setOrAdd(newP,newH,l2)
        l2 = l2.nxt
  return newH

def main():
  five = ListNode(5)
  three = ListNode(3,five)
  one = ListNode(1, three)

  four = ListNode(4)
  two = ListNode(2,four)
  head = mergeTwoLists(one,two)
  while (head):
    print head.val
    head = head.nxt

main()
