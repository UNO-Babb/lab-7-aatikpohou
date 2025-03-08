#Problem7.py
#Project Euler problem 7

from NumberTests import isEven
from NumberTests import fibonacciSequence
from NumberTests import isPrime

def main():
    nums = isPrime
    print (nums)
    
    """ Find the 10001 prime number"""
    count = 0
    num = 3

    while count < 10001:
       num +=1 
       if isPrime(num):
          count +=1
    return num


    


if __name__ == '__main__':
  main()


