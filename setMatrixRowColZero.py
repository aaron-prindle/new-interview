class Solution:
  # @param {integer[][]} matrix
  # @return {void} Do not return anything, modify matrix in-place instead.
  def setRowZero(self,matrix,row):
    for j in range(len(matrix[0])):
      matrix[row][j] = 0
  def setColZero(self,matrix,col):
    for i in range(len(matrix)):
      matrix[i][col] = 0

  def setZeroes(self, matrix):
    zeroes = []
    for row in range(len(matrix)):
      tmp = []
      for col in range(len(matrix[0])):
        if matrix[row][col] == 0:
          tmp.append(True)
        else:
          tmp.append(False)
      zeroes.append(tmp)
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if zeroes[row][col]:
          self.setRowZero(matrix,row)
          self.setColZero(matrix,col)
    

def main():
  solution = Solution()
  matrix = [[1,2,3],[1,2,3],[1,2,0]]
  print solution.setZeroes(matrix)
          
main()
