# Definition for a undirected graph node
class UndirectedGraphNode:
  def __init__(self, x):
    self.label = x
    self.neighbors = []

class Solution:
  def bfs(self,s):
    frontier = [s]
    clone_start = UndirectedGraphNode(s.label)
    clone_map = {s:clone_start}
    while frontier:
      nxt = []
      for u in frontier:
        for v in u.neighbors:
          if v not in clone_map:
            clone_v = UndirectedGraphNode(v.label)
            clone_map[u].neighbors.append(clone_v)
            clone_map[v] = clone_v
            nxt.append(v)
          else:
            clone_map[u].neighbors.append(clone_map[v])
      frontier = nxt
    return clone_start

  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    if not node:
      return None
    return self.bfs(node)
        
def main():
  pass
  solution = Solution()

  three = UndirectedGraphNode(3)
  two = UndirectedGraphNode(2)
  one = UndirectedGraphNode(1)
  one.neighbors = [one,one]
  print one
  out = solution.cloneGraph(one)
  print out
  print "----------------------------------------"
  for n in out.neighbors:
    print n.label
          
main()
