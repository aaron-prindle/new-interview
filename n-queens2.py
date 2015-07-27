def prn1(x):
  print x

def prn(lst):
  for i in lst:
    print i
  print "--------------------"

def solveNQueens(n):
  board = [['.']*n for i in range(n)]
  out = []
  queenSolver(0,board,out)
  return out

def canPlace(row,col,board):
  #left
  for j in range(col):
    if board[row][j] == 'Q':
      return False
  #up left
  i = row
  j = col
  while i>=0 and j>=0:
    if board[i][j] == 'Q':
      return False
    i-=1
    j-=1
  #up right
  i = row
  j = col
  while i<len(board) and j>=0:
    if board[i][j] == 'Q':
      return False
    i+=1
    j-=1
  return True

def queenSolver(col,board,out):
  if col >=len(board):
    tmp = []
    for row in board:
      for j in row:
        tmp.append(j)
    out.append(tmp)
    return False
  for row in range(len(board)):
    if canPlace(row,col,board):
      board[row][col] = 'Q'
      if queenSolver(col+1,board,out):
        return True
      board[row][col] = '.'
  return False

def main():
  n = 4
  print solveNQueens(4)
  
main()
