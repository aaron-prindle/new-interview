def arrayRotate(a):
  out = []
  rows = len(a)
  cols = len(a[0])
  for i in range(rows):
    new = []
    for j in range(cols):
      new.append(0)
    out.append(new)
    
  for i in range(rows):
    for j in range(cols):
      out[j][cols-1-i] = a[i][j]
  return out

def main():
  a = [[1,2,3],[4,5,6],[7,8,9]]
  rows = len(a)
  cols = len(a[0])
  out = arrayRotate(a)
  for i in range(rows):
    for j in range(cols):
        print a[i][j]

  print "========================================"

  for i in range(rows):
    for j in range(cols):
        print out[i][j]

main()
