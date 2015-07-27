class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        seenOne = False
        for i in range(64):
            if n & (1<<i):
                if seenOne:
                    return False
                else:
                    seenOne = True
        return seenOne

def main():
  solution = Solution()
  print solution.isPowerOfTwo(2)

main()
