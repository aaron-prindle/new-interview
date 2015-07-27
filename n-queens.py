def rowOk(board, row, col, N):
  for i in range(col):
    if board[row][i]:
      return False
  return True

def topLeftOk(board, row, col, N):
  i = row
  j = col
  while i>=0 and j>=0:
    if board[i][j]:
      return False
    i -= 1
    j -= 1
  return True

def bottomLeftOk(board, row, col, N):
  i = row
  j = col
  while i<N and j>=0:
    if board[i][j]:
      return False
    i += 1
    j -= 1
  return True

def canPlace(board, row, col, N):
  if not rowOk(board,row,col,N):
    return False
  if not topLeftOk(board,row,col,N):
    return False
  if not bottomLeftOk(board,row,col,N):
    return False
  return True

def boardSolver(board,col, N):
  if col >=N:
    return True
  for row in range(N):
    if canPlace(board,row,col,N):
      board[row][col] = True
      if boardSolver(board,col+1,N):
        return True
      board[row][col] = False
  return False

def prn(x):
  print x

def main():
  N = 4
  board = [[False]*N for i in range(N)]
  print boardSolver(board, 0, N)
  map(prn, board)
  
main()
