class TriStack:
  def __init__(self,n):
    self.tops = [None] * 3
    self.array = [None] * n
    self.lBounds = [None] * 3
    self.hBounds = [None] * 3
    for i in range(3):
      self.lBounds[i] = i*n/3
      self.tops[i] = i*n/3
      self.hBounds[i] = (i+1)*n/3-1

  def pop(self,id):
    if self.isEmpty(id):
      return
    data = self.array[self.tops[id]]
    self.tops[id] -= 1
    return data

  def push(self,id,data):
    if self.isFull(id):
      return
    self.tops[id] +=1
    self.array[self.tops[id]] = data

  def isEmpty(self,id):
    if self.tops[id] < self.lBounds[id]:
      return True
    return False

  def isFull(self,id):
    if self.tops[id] >= self.hBounds[id]:
      return True
    return False
    
    
      
def main():
  triStack = TriStack(9)
  triStack.push(0,1)
  triStack.push(1,2)
  triStack.push(2,3)
  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)

  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)

  triStack.push(0,1)
  triStack.push(1,2)
  triStack.push(2,3)
  triStack.push(0,1)
  triStack.push(1,2)
  triStack.push(2,3)
  triStack.push(0,1)
  triStack.push(1,2)
  triStack.push(2,3)
  triStack.push(0,1)
  triStack.push(1,2)
  triStack.push(2,3)

  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)
  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)
  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)
  print triStack.pop(0)
  print triStack.pop(1)
  print triStack.pop(2)


main()
