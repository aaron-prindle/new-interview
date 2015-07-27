def twoSum(self,nums,target):
  dict = {}
  for i in range(len(nums)):
    if n[i] in dict:
      return [map[n[i]], i]
    else:
      map[target-n[i]] = i
