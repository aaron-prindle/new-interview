def strCompression(s):
  out = []
  count = 0
  last = s[0]
  for c in s:
    if c==last:
      count +=1
    else:
      out.append(last)
      out.append(str(count))
      last = c
      count = 1
  out.append(last)
  out.append(str(count))
  s_out = ''.join(out)
  if len(s)<=len(s_out):
    return s
  return s_out

def main():
  s = "aaabbaacc"
  print strCompression(s)

main()
