class TreeNode:
  def __init__(self,val,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

def sumDFS(root,summ,count,path):
  path.append(root.val)
  if root.left==None and root.right == None:
    for i in range(len(path)):
      summ[0] += path[i]*10**(len(path)-1-i)
    return
  print path
  sumDFS(root.left,summ,count+1,path[:])
  sumDFS(root.right,summ,count+1,path[:])


def sumNumbers(root):
  summ = [0]
  sumDFS(root,summ,0,[])
  return summ[0]
  

def main():
  three = TreeNode(3)
  two = TreeNode(2)
  one = TreeNode(1,two,three)
  print sumNumbers(one)

main()
