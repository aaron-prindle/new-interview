import math

def primeGen(n):
  sieve = [False]*n
  i = 2
  out = []
  while i<n:
    if sieve[i] == False:
      out.append(i)
      for j in range(i*i,n,i):
        sieve[j] = True
      #set all values in between
    i+=1
  return out

def main():
  print primeGen(1000)

main()
