import pdb


def isleCheck(grid,i,j,n,m):
  if i<0 or i>n-1 or j<0 or j>m-1:
    return
  if grid[i][j] == '1':
    grid[i][j] = 's'
    isleRecurse(grid,i,j,n,m)

def isleRecurse(grid,i,j,n,m):
  isleCheck(grid,i+1,j,n,m)
  isleCheck(grid,i-1,j,n,m)
  isleCheck(grid,i,j+1,n,m)
  isleCheck(grid,i,j-1,n,m)

def numIslands(grid):
  count = 0
  n = len(grid)
  m = len(grid[0])
  for i in range(n):
    for j in range(m):
      if grid[i][j] == '1':
        grid[i][j] = 's'
        count +=1
        isleRecurse(grid,i,j,n,m)
        #pdb.set_trace()
  print count
  return grid

def prn(x):
  print x

def main():
  grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
  map(prn,numIslands(grid))

main()
