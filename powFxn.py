def powFxn(base,exp):
  if exp == 0:
    return 1
  elif exp < 0:
    return 1.0 / powFxn(base,-exp)
  elif exp % 2 == 0:
    half_pow = powFxn(base,exp // 2)
    return half_pow*half_pow
  else:
    return base * powFxn(base,exp-1)

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x,-n)
        elif n % 2 == 0:
            half_pow = self.myPow(x,n//2)
            return half_pow * half_pow
        else:
            return x * self.myPow(x,n-1)

def main():
  print powFxn(2,6)
  solution = Solution()
  print solution.myPow(2,6)

main()
