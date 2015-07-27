from sys import maxint

def maxProfit(prices):
  curMin = prices[0]
  curMinI = 0
  curMax = prices[1]
  curMaxI = 1
  if prices[1] < prices[0]:
    pMin = prices[1]
    pMinI = 1
  else:
    pMin = curMin
    pMinI = curMinI
  pMax = curMax
  pMaxI = curMaxI
  for i in range(2,len(prices)):
    if prices[i] <=  pMin:
      pMin = prices[i]
      pMinI = i
      pMax = -maxint
    if prices[i] > pMax:
      pMax = prices[i]
      pMaxI = i
    if pMinI < pMaxI and pMax - pMin > curMax-curMin:
      curMin = pMin
      curMinI = pMinI
      curMax = pMax
      curMaxI = pMinI
  return curMax-curMin

def main():
  prices = [7,12,20,1,4,15]
  print maxProfit(prices)
  three= [100,1,7]
  print maxProfit(three)
  two= [100,5]
  print maxProfit(two)
  two2= [5,100]
  print maxProfit(two2)


main()
      
