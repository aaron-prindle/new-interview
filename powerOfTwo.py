def isPowerOfTwo(n):
  seenOne = False
  for i in range(64):
    if n & (1<<i):
      if seenOne:
        return False
      else:
        seenOne = True
  return seenOne

def main():
  print isPowerOfTwo(2)
main()
