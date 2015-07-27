def magicNumber(arr):
  if not arr:
    return -1
  return magicSearch(arr,0,len(arr)-1)
  
def magicSearch(arr,low,high):
  mid = (low+high)/2
  if arr[mid] < mid:
    return magicSearch(arr,mid+1,high)
  elif arr[mid] > mid:
    return magicSearch(arr,low,mid-1)
  else:
    return mid
  
def main():
  arr = [-1,0,1,2,4,8]
  print magicNumber(arr)

main()
