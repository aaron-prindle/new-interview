class Solution:
  # @param {integer} numCourses
  # @param {integer[][]} prerequisites
  # @return {integer[]}
  def findOrder(self, numCourses, prerequisites):
    Adj = {}
    for i in range(numCourses):
      Adj[i] = []
    for course,dependancy in prerequisites:
      Adj[dependancy].append(course)
    seen = set()
    order = []
    hasCycle = [False]
    for u in Adj:
      if u not in seen:
        seen.add(u)
        traversed = [u]
        self.DFS(Adj,u,seen,order,traversed,hasCycle)
        traversed.pop()
    if hasCycle[0]:
      return []
    return order[::-1]
        
  def DFS(self,Adj,u,seen,order,traversed,hasCycle):
    for v in Adj[u]:
      if v in traversed:
        hasCycle[0] = True
      if v not in seen:
        seen.add(v)
        traversed.append(v)
        self.DFS(Adj,v,seen,order,traversed,hasCycle)
        traversed.pop()
    order.append(u)

def main():
  solution = Solution()
  numCourses = 4
  prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  print solution.findOrder(numCourses,prerequisites)
  numCourses = 2
  prerequisites = [[1,0],[0,1]]
  print solution.findOrder(numCourses,prerequisites)
  numCourses = 8
  prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
  print solution.findOrder(numCourses,prerequisites)

main()
