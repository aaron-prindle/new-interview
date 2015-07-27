class Node:
  def __init__(self,key=None,nxt=None):
    self.key = key
    self.nxt = nxt

class BTreeNode:
  def __init__(self,key=None,left=None,right=None):
    self.key = key
    self.left = left
    self.right = right

def BFS(s):
  #BFS
  #create linked list at levels
  frontier = [s]
  levels = {0:[s.key]}
  i = 1
  while frontier:
    nxt = []
    for n in frontier:
      if n.left:
        if not levels.get(i,None):
          levels[i] = [n.left.key]
        else:
          levels[i].append(n.left.key)
        nxt.append(n.left)
      if n.right:
        if not levels.get(i,None):
          levels[i] = [n.right.key]
        else:
          levels[i].append(n.right.key)
        nxt.append(n.right)
    i +=1
    frontier = nxt
  return levels
      

def linkedListFromBTree(n):
  levels = BFS(n)
  out = []
  for k,v in levels.iteritems():
    head = Node(v[0])
    out.append(head)
    for i in range(1,len(v)):
      head.nxt = Node(v[i])
      head = head.nxt
  return out

def main():
  eight = BTreeNode(8,None,None)
  seven = BTreeNode(7,None,None)
  three = BTreeNode(3,seven,eight)
  two = BTreeNode(2,None,None)
  one = BTreeNode(1,two,three)
  ll = linkedListFromBTree(one)
  for n in ll:
    cur = n
    while (n!=None):
      print n.key,
      n = n.nxt
    print

main()
