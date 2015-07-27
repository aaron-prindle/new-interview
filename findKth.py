class Node:
  def __init__(self,key=None, nxt=None):
    self.key = key
    self.nxt = nxt

def findKthLast(head, k):
  cur = head
  kth = None
  count = 0
  while(cur!=None):
    if count == k-1:
      kth = head
    elif count>=k:
      kth = kth.nxt
    count+=1
    cur = cur.nxt
  return kth

def main():
  five = Node("five", None)
  four = Node("four", five)
  three = Node("three", four)
  two = Node("two", three)
  one = Node("one", two)
  print findKthLast(one,2).key

main()
