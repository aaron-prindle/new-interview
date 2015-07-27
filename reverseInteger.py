import math


def reverseInteger(x):
  if x == 0:
    return 0
  isNeg = False
  if x < 0:
    isNeg = True
    x *= -1
  tens = int(math.log10(x))
  summ = 0
  for i in range(0,tens+1):
    cur = x/(10**(tens-i))
    summ += cur * 10**i
    x -= cur * (10**(tens-i))
    print x
  if isNeg:
    summ *= -1
  return summ

def main():
  x = -123
  print reverseInteger(x)

main()
