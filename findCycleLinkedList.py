class Node:
  def __init__(self,key=None,nxt=None):
    self.key = key
    self.nxt = nxt

def findCycleLinkedList(head):
  sp = head
  fp = head
  if (sp == fp):
    print "SAME"
  if (head.nxt == None or head.nxt.nxt == None):
    return None
  sp = head.nxt
  fp = head.nxt.nxt
  while (fp and sp and sp!=fp):
    sp = sp.nxt
    if fp.nxt == None:
      return None
    fp = fp.nxt.nxt
    print sp.key, fp.key
  if(fp == None):
    return None
  sp = head
  while(sp!=fp):
    sp = sp.nxt
    fp = fp.nxt
  return sp
    

def main():
  # five = Node(5,None)
  # four = Node(4,five)
  # three = Node(3,four)
  # two = Node(2,three)
  # one = Node(1,two)
  # print findCycleLinkedList(one)

  three = Node(3,None)
  five = Node(5,three)
  four = Node(4,five)
  three.nxt = four
  two = Node(2,three)
  one = Node(1,two)
  print findCycleLinkedList(one).key


main()
