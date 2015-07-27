class ListNode:
  def __init__(self,data,nxt = None):
    self.data = data
    self.nxt = nxt

class Queue:
  def __init__(self):
    self.first = None
    self.last = None

  def enqueue(self,data):
    new = ListNode(data)
    if not self.first:
      self.last= new
      self.first = self.last
      return
    self.last.nxt = new
    self.last= self.last.nxt
    

  def dequeue(self):
    if not self.first:
      return self.first
    data = self.first.data
    self.first = self.first.nxt
    if not self.first:
      self.last = None
    return data
    

def main():
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  print queue.dequeue()
  print queue.dequeue()
  print queue.dequeue()
  print queue.dequeue()
  print queue.dequeue()


main()
