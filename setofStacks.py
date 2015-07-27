class Node:
  def __init__(self,key = None, nxt = None):
    self.key = key
    self.nxt = nxt

class Stack:
  def __init__(self):
    self.top = None
    self.length = 0

  def pop(self):
    if self.isEmpty():
      return None
    key = self.top.key
    self.top = self.top.nxt
    self.length -= 1
    return key

  def push(self,key):
    new = Node(key)
    if self.isEmpty():
      self.top = new
      return
    new.nxt = self.top
    self.top = new
    self.length += 1
  
  def isEmpty(self):
    if self.top == None:
      return True
    return False

class SetOfStacks:
  def __init__(self,N):
    self.stacks = []
    self.stacks.append(Stack())
    self.N = N
  
  def push(self,key):
    lastI = len(self.stacks)-1
    if self.stacks[lastI].length >= self.N:
      self.stacks.append(Stack())
      self.stacks[lastI+1].push(key)
      return
    self.stacks[lastI].push(key)
  
  def pop(self):
    lastI = len(self.stacks)-1
    if len(self.stacks) == 1:
      #HERE-1
      return self.stacks[lastI].pop()
    key = self.stacks[lastI].pop()
    if key == None:
      self.stacks.pop()
      return self.stacks[lastI-1].pop()
    #HERE-2
    return key
  
  def isEmpty(self):
    if len(self.stacks) == 1:
      if self.stacks[len(self.stacks)-1].isEmpty():
        return True
    return False

def main():
  setOfStacks = SetOfStacks(2)
  setOfStacks.push(1)
  setOfStacks.push(2)
  setOfStacks.push(3)
  setOfStacks.push(4)
  setOfStacks.push(5)
  print setOfStacks.pop()
  print setOfStacks.pop()
  print setOfStacks.pop()
  print setOfStacks.pop()
  print setOfStacks.pop()
  print setOfStacks.pop()

main()
