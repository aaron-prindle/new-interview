def bfs(s,Adj):
  parent = {s:None}
  frontier = [s]
  level = {}
  i = 1
  while frontier:
    nxt = []
    for u in frontier:
      for v in Adj[u]:
        if v not in parent:
          parent[v] = u
          level[v] = i
          nxt.append(v)
    i+=1
    frontier = nxt
  return parent

def main():
  Adj = {"a":["b","c"],"b":["c"],"c":["d"],"d":[]}
  s = "a"
  print bfs(s,Adj)

main()
