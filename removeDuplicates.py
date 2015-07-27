class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
      seen = set()
      pointer = 0
      for i in range(len(nums)):
          if nums[i] not in seen:
            nums[pointer] = nums[i]
            pointer+=1
            seen.add(nums[i])
      return pointer

def main():
  solution = Solution()
  nums = [1,1,2]
  print solution.removeDuplicates(nums)
  print nums

main()
