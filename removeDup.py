class Node:
  def __init__(self,key=None, nxt=None):
    self.key = key
    self.nxt = nxt

def removeDup(head):
  seen = {}
  last = None
  while(head!=None):
    if seen.get(head.key, None):
      remove(last, head)
    else:
      seen[head.key] = True
    last = head
    head = head.nxt

def remove(last,cur):
  last.nxt = cur.nxt
  print cur.key
  del cur


def main():
  one2 = Node("one", None)
  three2 = Node("three", one2)
  three = Node("three", three2)
  two = Node("two", three)
  one = Node("one", two)
  removeDup(one)

main()
