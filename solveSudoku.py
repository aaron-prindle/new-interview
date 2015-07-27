def prn(x):
  print x

def solveSudoku(board):
  return sudokuRecurse(board)

def rowOk(row,col,board):
  seen = set()
  for i in range(len(board[0])):
    if board[row][i] in seen:
      return False
    elif board[row][i] != '.':
      seen.add(board[row][i])
  return True

def colOk(row,col,board):
  seen = set()
  for i in range(len(board)):
    if board[i][col] in seen:
      return False
    elif board[i][col] != '.':
      seen.add(board[i][col])
  return True

def findSubmatrix(row,col,board):
  sRow = 0
  eRow = 0
  sCol = 0
  eCol = 0
  for i in range(len(board)/3):
    sRow = len(board)//3 * i
    eRow = len(board)//3 * (i+1) -1
    if sRow <= row <= eRow:
      break
  for i in range(len(board[0])/3):
    sCol = len(board[0])//3 * i
    eCol = len(board[0])//3 * (i+1) -1
    if sCol <= col <= eCol:
      break
  return sRow,eRow,sCol,eCol


def boxOk(row,col,board):  
  seen = set()
  sRow,eRow,sCol,eCol = findSubmatrix(row,col,board)
  for i in range(sRow,eRow+1):
    for j in range(sCol,eCol+1):
      if board[i][j] in seen:
        return False
      elif board[i][j] != '.':
        seen.add(board[i][j])
  return True

def checkVal(row,col,board):
  if not rowOk(row,col,board):
    return False
  if not colOk(row,col,board):
    return False
  if not boxOk(row,col,board):
    return False
  return True

def sudokuRecurse(board):
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == '.':
        for val in "123456789":
          print row,col
          map(prn,board)
          print "------------------------------"
          board[row][col] = val
          if checkVal(row,col,board):
            if sudokuRecurse(board):
              return True
          board[row][col] = '.'
        return False
  return True
            

def main():
  board = [
  ['5','3','.','.','7','.','.','.','.'],
  ['6','.','.','1','9','5','.','.','.'],
  ['.','9','8','.','.','.','.','6','.'],
  ['8','.','.','.','6','.','.','.','3'],
  ['4','.','.','8','.','3','.','.','1'],
  ['7','.','.','.','2','.','.','.','6'],
  ['.','6','.','.','.','.','2','8','.'],
  ['.','.','.','4','1','9','.','.','5'],
  ['.','.','.','.','8','.','.','7','9']]
  #n = 9  
  #board = [['.']*n for i in range(n)]
  solveSudoku(board)
  map(prn,board)
main()
