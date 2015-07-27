class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix:
          return matrix
        up = 0; left = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        direct = 0
        out = []
        while True:
          if direct == 0:
            for col in range(left,right+1):
              out.append(matrix[up][col])
            up+=1
          if direct == 1:      
            for row in range(up,down+1):
              out.append(matrix[row][right])
            right-=1
          if direct == 2:
            for col in range(right,left-1,-1):
              out.append(matrix[down][col])
            down-=1
          if direct == 3:
            for row in range(down,up-1,-1):
              out.append(matrix[row][left])
            left+=1
          if up > down or left > right:
            return out
          direct = (direct+1)%4

def main():
  arr = [[1,2,3],[4,5,6],[7,8,9]]
  #arr = [[2,3]]
  solution = Solution()
  print solution.spiralOrder(arr)

main()

#[[2,3]]
#[[3],[2]]
