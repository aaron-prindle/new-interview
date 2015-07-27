def findPathDFS(s,e,Adj):
  done = False
  parent = {}
  DFSRecurse(s,e,Adj,parent,done)
  n = e
  path = []
  while(n!=s):
    path.append(n)
    n = parent[n]
  path.append(n)
  path.reverse()
  print parent.get("d",None)
  return path

def DFSRecurse(s,e,Adj,parent,done):
  for u in Adj[s]:
    if done:
      return
    if u not in parent:
      parent[u] = s
      if u == e:
        done = True
        return
      DFSRecurse(u,e,Adj,parent,done)

def BFS(s,e,Adj):
  frontier = [s]
  parent = {s:None}
  level = {s:0}
  i = 1
  while frontier:
    for u in frontier:
      nxt = []
      for v in Adj[u]:
        if v not in parent:
          level[v] = i
          parent[v] = u
          if v == e:
            return parent
          nxt.append(v)
    frontier = nxt
    i+=1

def findPathBFS(s,e,Adj):
  parent = BFS(s,e,Adj)
  n = e
  path = []
  while(n!=s):
    path.append(n)
    n = parent[n]
  path.append(n)
  path.reverse()
  return path


def main():
  Adj = {"a":["b"], "b":["c"], "c":["d"], "d":["a"]}
  s = "a"
  e = "c"
  print findPathDFS(s,e,Adj)
  print findPathBFS(s,e,Adj)

main()
