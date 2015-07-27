def DFS(self, leftChild, moves, count, lefts, string, out, n):
  if moves == 2*n and lefts == n:
    out.append(string)
    return
  if leftChild:
    count+=1
    moves+=1
    lefts+=1
    string += "(" #slow
  else:
    count-=1
    moves+=1
    string += ")" #slow
  if count < n and lefts <= n:
    DFS(True,moves,count,lefts,string,out,n)
  if count > 0:
    DFS(False,moves,count,lefts,string,out,n)
    
  

def generateParenthesis(self, n):
  out = []
  DFS(True,0,0,0,"",out, n)
  return out

def main():
  print generateParenthesis(3)

main()
