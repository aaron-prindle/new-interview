#questions, should i check to make sure there is enough space?
#A is null?
#B is null?
#A is empty?
#B is empty?

def mergeSortedArrays(A,aP,B):
  aS = 0
  bS = 0
  bP = len(B)-1
  cur = len(A)-1
  while bP>=bS:
    print aP
    print bP
    print "========================================"
    if aP >= 0 and A[aP] > B[bP]: #I fucked this up, forgot aP>=0
      A[cur] = A[aP]
      aP -= 1
    else:
      A[cur] = B[bP]
      bP -= 1
    cur -=1

def main():
  A = [-1,1,3,5,0,0,0,0] 
  B = [-2,0,2,4]
  mergeSortedArrays(A,3,B)
  print A

main()
