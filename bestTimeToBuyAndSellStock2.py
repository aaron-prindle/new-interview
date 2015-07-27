from sys import maxint

def maxProfit(prices):
  if len(prices)<2:
    return 0
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
  summ = 0
  hasChanged = True
  for i in range(2,len(prices)):
    if prices[i] <=  pMin:
      hasChanged = True
      pMin = prices[i]
      pMinI = i
      pMax = -maxint
    if prices[i] > pMax:
      pMax = prices[i]
      pMaxI = i
    if pMinI < pMaxI and hasChanged: #and pMax - pMin > curMax-curMin:
      hasChanged = False
      if curMax-curMin > 0:
        summ += curMax-curMin
        print summ
        print curMax, curMin
      curMin = pMin
      curMinI = pMinI
      curMax = pMax
      curMaxI = pMinI
  diff = curMax - curMin
  if diff <0:
    return 0
  print "----------------------------------------"
  return summ + diff

def main():
  prices = [7,12,20,1,4,15]
  print maxProfit(prices)
  three= [100,1,7]
  print maxProfit(three)
  two= [100,5]
  print maxProfit(two)
  two2= [5,100]
  print maxProfit(two2)
  fail= [1,2,4]
  print maxProfit(fail)


main()
      
