#Problem7.py
#Project Euler problem 7

from NumberTests import isEven
from NumberTests import fibonacciSequence
from NumberTests import isPrime

def main():
   """List of all prime number"""
   primeCount = 0
   num = 1
   while primeCount < 10001:
      num = num + 1
      if isPrime(num):
         primeCount = primeCount + 1
         print (num)
"""def list_primes(n): 
    return [num for num in range(2, n + 1) if isPrime(num)]


n = 105000

 #print(list_primes(n))

list1 = list_primes(n)

print(list1[10001])"""



if __name__ == '__main__':
  main()


