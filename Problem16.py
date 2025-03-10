#Problem16.py
#Project Euler problem 16

"""Create an exponant function"""

def  expo (e):
    e = 1000
    n = 2
    expo = n ** e
   
    print([expo])
    digits(expo)

"""the sum of the digits"""
def digits(d):
    d = str(d)
    total = 0
    for digit in d:
        digit = int(digit)
        total = total + digit
    
    """
            digits = expo
    digits_expo = int(digits)
    sum = sum(digits_expo)"""

    print(total)


if __name__ == '__main__':
    expo(5) #call expo function