    def isValid(s):
      closers = ["(","[","{"]
      openers_map = {")":"(", "]":"[", "}":"{"}
      stack = []
      for c in s:
        if c in closers: #is an opener
          stack.append(c)
        else: # is a closer
          if len(stack) == 0:
            return False
          opener = stack.pop()
          closer = openers_map[c]
          if closer != opener:
            return False
      if len(stack) !=0:
        return False
      return True

def main():
  test = "())"
  print isValid(test)

main()
