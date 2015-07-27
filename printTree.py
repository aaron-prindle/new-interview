class Node:
  def __init__(self, key=None, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

  def _str__(self):
    return str(self.key)

def printTree(n):
  levelDict = {}
  inOrderRecurse(n,0,levelDict)
  i=0
  while(levelDict.get(i,None)):
      for k in levelDict[i]:
        print k,
      print
      i+=1

def inOrderRecurse(n,level,levelDict):
  if n==None:
    return
  #left
  inOrderRecurse(n.left,level+1,levelDict)
  #self
  if levelDict.get(level,None):
    levelDict[level].append(n.key)
  else:
    levelDict[level] = [n.key]
  #right
  inOrderRecurse(n.right,level+1,levelDict)

def main():
  four = Node(4,None,None)
  three = Node(3,None,None)
  one = Node(1,four, None)
  two = Node(2,one,three)
  printTree(two)

main()
