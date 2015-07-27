class Node:
  def __init__(self,key=None,nxt=None):
    self.key = key
    self.nxt = nxt

class Stack:
  def __init__(self):
    self.top = None
    self.minT = None

  def pop(self):
    if self.isEmpty():
      return None
    key = self.top.key
    self.top = self.top.nxt
    self.minT = self.minT.nxt
    return key

  def push(self,key):
    if self.isEmpty():
      self.top = Node(key)
      self.minT = Node(key)
      return
    new = Node(key)
    new.nxt = self.top
    self.top = new
    minK = self.minT.key
    if(key<=self.minT.key):
      minK=key
    minN = Node(minK)
    minN.nxt = self.minT
    self.minT = minN
  
  def isEmpty(self):
    if self.top == None and self.minT == None:
      return True
    return False

  def min(self):
    if self.isEmpty():
      return None
    return self.minT.key


def main():
  stack = Stack()
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  stack.push(1)
  print stack.min()
  print stack.pop()
  print "----------------------------------------"
  print stack.min()
  print stack.pop()
  print "----------------------------------------"
  print stack.min()
  print stack.pop()
  print "----------------------------------------"
  print stack.min()
  print stack.pop()
  print "----------------------------------------"
  print stack.min()
  print stack.pop()
  print "----------------------------------------"
  print stack.min()
  print stack.pop()


main()
