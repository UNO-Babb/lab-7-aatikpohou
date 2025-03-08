#Problem10.py
#Project Euler problem 10

from NumberTests import isEven
from NumberTests import fibonacciSequence
from NumberTests import isPrime
def main():
   """List of all prime number"""
def list_primes(n):
    return [num for num in range(2, n + 1) if isPrime(num)]


n = 2000000

print(list_primes(n))

list1 = list_primes(n)
sum = sum(list1)
print(sum)


if __name__ == '__main__':
  main()
