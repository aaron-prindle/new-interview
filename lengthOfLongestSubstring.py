def lengthOfLongestSubstring(s):
  seen = {}
  tail = 0
  maxx = 0
  for i in range(len(s)):
    c = s[i]
    if c in seen:
      if tail < seen[c]:
        tail = seen[c]+1
      seen[c] = i
    else:
      seen[c] = i
    if (i - tail) > maxx:
      maxx = i - tail
  return maxx

def main():
  s = "bbbbb"
  print lengthOfLongestSubstring(s)
  s = "abcabcbb"
  print lengthOfLongestSubstring(s)
  s = "abba"
  print lengthOfLongestSubstring(s)


main()
