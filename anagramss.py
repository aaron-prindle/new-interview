# @param {string[]} strs
# @return {string[]}
def anagrams(strs):
  out = []
  anagramDict = {}
  anagramSet = set()
  for word in strs:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagramDict:
      anagramDict[sortedWord].append(word)
    else:
      anagramDict[sortedWord] = [word]
  for key in anagramDict:
    words = anagramDict[key]
    if len(words)>1:
      for word in words:
        out.append(word)
  return out
  

def main():
  strs = "god","dog","bar","bra","hello"
  print anagrams(strs)

main()
