def searchRange(nums,target):
  low,mid,high = binarySearch(nums,0,len(nums)-1,target,True)
  low2,mid2,high2 = binarySearch(nums,low,mid-1,target-.5,False)
  low3,mid3,high3 = binarySearch(nums,mid+1,high,target+.5,False)
  return [low2,high3]

def binarySearch(nums,low,high,target,isTarget):
  if low>high:
    if isTarget:
      return -1,-1,-1
    return low,0,high
  mid = (low+high)/2
  if nums[mid]<target:
    return binarySearch(nums,mid+1,high,target,isTarget)
  elif nums[mid]>target:
    return binarySearch(nums,low,mid-1,target,isTarget)
  else:
    return low,mid,high

#
def main():
  target = 9
  nums = [1,2,9,9,9,9,10,11,12,13]
  low,mid,high = binarySearch(nums,0,len(nums)-1,target,True)
  low2,mid2,high2 = binarySearch(nums,low,mid-1,target-.5,False)
  low3,mid3,high3 = binarySearch(nums,mid+1,high,target+.5,False)
  print low2,high3
main()
