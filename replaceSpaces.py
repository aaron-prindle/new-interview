def replaceSpaces(arr,n):
  high = len(arr)-1
  for low in range(n-1,-1,-1):
    if arr[low] == ' ':
      arr[high] = '0'
      arr[high-1] = '2'
      arr[high-2] = '%'
      high -=3
    else:
      arr[high] = arr[low]
      high -=1
  return arr

def main():
  arr = ['a',' ', 'b',' ',' ']
  print replaceSpaces(arr,3)

main()
