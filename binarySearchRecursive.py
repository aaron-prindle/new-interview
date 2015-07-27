# def binarySearch(a,X,l,h):
#   mid = (l+h) / 2
#   if l==h:
#     return mid
#   if a[mid]<X:
#     return binarySearch(a,X,mid+1,h)
#   elif a[mid]>X:
#     return binarySearch(a,X,l,mid-1)
#   else :
#     return mid
  
# def main():
#   a = [1,3,4,6]
#   print binarySearch(a,5,0,len(a)-1)

# main()


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self.binarySearch(nums,target,0,len(nums)-1)
        
    def binarySearch(self,a,X,l,h):
        mid = (l+h)/2
        if l == h:
            if a[mid] > X and mid!=0:
              return mid - 1
            elif a[mid] < X:
              return mid + 1
            elif mid == 0:
              return 0
            else :
              return mid
            
        if a[mid] < X:
            return self.binarySearch(a,X,mid+1,h)
        elif a[mid] > X:
            return self.binarySearch(a,X,l,mid-1)
        else:
            return mid

def main():
  solution = Solution()
  a = [1,3,5,6]
  print solution.searchInsert(a,5)
  a = [1,3,5,6]
  print solution.searchInsert(a,2)
  a = [1,3,5,6]
  print solution.searchInsert(a,7)
  a = [1,3,5,6]
  print solution.searchInsert(a,0)


main()
