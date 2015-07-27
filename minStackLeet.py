class ListNode:
  def __init__(self,val):
    self.val = val
    self.nxt = None

class MinStack:
  # initialize your data structure here.
  def __init__(self):
    self.top = None
    self.minTop = None

  # @param x, an integer
  # @return nothing
  def push(self, x):
    new = ListNode(x)
    if not self.top:
      self.top = new
      self.minTop = new
    else:
      new.nxt = self.top
      self.top = new
      minVal = self.getMin()
      if x < self.getMin():
        minVal = x
      newMin = ListNode(minVal)
      newMin.nxt = self.minTop
      self.minTop = newMin
        
      
  # @return nothing
  def pop(self):
    if not self.top:
      return
    val = self.top.val
    self.top = self.top.nxt
    self.minTop = self.minTop.nxt
    return val
      
  # @return an integer
  def top(self):
    if self.top:
      return self.top.val
    return None
      
  # @return an integer
  def getMin(self):
    if self.minTop:
      return self.minTop.val
    return None
      
def main():
  minStack = MinStack()
  minStack.push(1)
  minStack.push(2)
  minStack.push(3)
  minStack.getMin()
  print minStack.pop()
  minStack.getMin()
  print minStack.pop()
  minStack.getMin()
  print minStack.pop()
  minStack.getMin()
  print minStack.pop()

main()
