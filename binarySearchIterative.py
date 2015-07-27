def binarySearch(a,X):
  l = 0
  h = len(a)-1
  while (l<=h):
    mid = (l+h) // 2
    if a[mid] < X:
      l = mid+1
    elif a[mid] > X:
      h = mid-1
    else:
      return mid
  return -1
