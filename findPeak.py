def findPeakElement(nums):
  return peakSearch(nums,0,len(nums)-1)
  
def isPeak(arr,index):
  l = -1
  r = -1
  way = ""
  if index!=0:
    l = arr[index-1]
    way = "right"
  if index != len(arr)-1:
    r = arr[index+1]
    way = "left"
  if  l < arr[index] > r :
    return True,way
  return False,way

def peakSearch(arr,low,high):
  mid = (low+high)/2
  truePeak,way = isPeak(arr,mid)
  if truePeak:
    return mid
  elif (way and way=="right") or arr[mid] < arr[mid+1]:
    return peakSearch(arr,mid+1,high)
  else:
    return peakSearch(arr,low,mid-1)

def main():
  arr = [1,2,3,1]
  print findPeakElement(arr)

main()
