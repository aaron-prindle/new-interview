def findRepeatedDnaSequences(s):
  subSeqLen = 10
  out = []
  if len(s) <10:
    return out
  low = 0
  high = subSeqLen-1
  seen = {}
  while high < len(s):
    slce = s[low:high+1]
    subSeq = "".join(slce)
    if subSeq in seen and not seen[subSeq]:
      out.append(subSeq)
      seen[subSeq] = True
    if subSeq not in seen:
      seen[subSeq] = False
    low+=1
    high+=1
  return out
    
  

def main():
  s = "AAAAAAAAAAAAA"
  print findRepeatedDnaSequences(s)


main()
