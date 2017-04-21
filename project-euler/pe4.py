#Created by biracruz on 23 May 2012.

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 � 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys

def main():
    largest = -1
    for firstNumber in range(999,100,-1):
        for secondNumber in range(999,100,-1):
            number = firstNumber*secondNumber
            if str(number)==str(number)[::-1] and number > largest:
                largest = number
    print largest

if __name__=='__main__':
    main()
