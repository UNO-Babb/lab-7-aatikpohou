#Problem10.py
#Project Euler problem 10

from NumberTests import isEven
from NumberTests import fibonacciSequence
from NumberTests import isPrime
def main():
    nums = fibonacciSequence(2000001)
    print (nums)
    total = 0
    for fib in nums:
        if isEven(fib):
            total = total + fib
  
    print(total) # final answer