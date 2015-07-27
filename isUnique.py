def isUnique(str):
  seen = {}
  for c in str:
    if seen.get(c, None):
      return False
    else:
      seen[c] = True
  return True

def main():
  str = "a"
  print isUnique(str)
  str = "aa"
  print isUnique(str)
  str = "abc"
  print isUnique(str)
  str = ""
  print isUnique(str)
  str = "abcc"
  print isUnique(str)

main()
