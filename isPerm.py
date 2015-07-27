def isPerm(s1,s2):
  if len(s1)!=len(s2):
    return False
  seen = {}
  for c in s1:
    if seen.get(c,None):
      seen[c]+=1
    else:
      seen[c]=1
  for c in s2:
    if seen.get(c,None):
      seen[c]-=1
      if seen[c]<0:
        return False
    else:
      return False

  for k in seen:
    if seen[k]!=0:
      return False
  return True

def main():
  s1 = "abccb"
  s2 = "cabca"
  print isPerm(s1,s2)

main()
