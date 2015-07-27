class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
      start = 0
      end = len(nums)
      out = []
      self.permRecurse(nums,out,start,end)
      return out

    def permRecurse(self,nums,out,start,end):
      if start == end-1:
        if nums not in out:
          out.append(nums[:])
      else:
        x = nums[:]
        for current in range(start,end):
          temp = x[start]
          x[start] = x[current]
          x[current] = temp
          self.permRecurse(x,out,start+1,end)
          temp = x[start]
          x[start] = x[current]
          x[current] = temp

def main():
  nums = [1]
  solution = Solution()
  print solution.permute(nums)
  

main()
