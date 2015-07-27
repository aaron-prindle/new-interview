class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]

def main():
  solution = Solution()
  num = [3,30,34,5,9]
  print solution.largestNumber(num)
  num = [0,1,2,3,4,5]
  print solution.largestNumber(num)
  print solution.compare('1','2')

  
main()
