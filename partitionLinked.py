class Node:
  def __init__(self,key=None, nxt=None):
    self.key = key
    self.nxt = nxt

def partitionLinked(head, target):
  lPointer = None
  gPointer = None
  gHead = None
  lHead = None
  cur = head
  while(cur!=None):
    if cur.key < target:
      if(lPointer == None):
        lPointer = cur
        lHead = cur
      else:
        lPointer.nxt = cur
        lPointer = cur
    else:
      if(gPointer == None):
        gPointer = cur
        gHead = cur
      else:
        gPointer.nxt = cur
        gPointer = cur
    cur = cur.nxt #forgot
  gPointer.nxt = None
  if lPointer != None:
    lPointer.nxt = gHead
  return lHead

def main():
  one = Node(1, None)
  two = Node(2, one)
  three = Node(3, two)
  four = Node(4, three)
  five = Node(5, four)
  lHead =  partitionLinked(five,3)
  while(lHead):
    print lHead.key
    lHead = lHead.nxt

main()
