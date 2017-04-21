#Created by biracruz on 23 May 2012.

"""
Find the largest prime factor of a composite number.
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import sys

def main():
    for factor in prime_factors(600851475143):
        print factor
    
def prime_factors(number):
    divisor = 2
    current = number
    factors = []
    while(current > 1):
        if current % divisor == 0:
            current = current / divisor
            factors.append(divisor)
        else:
            if divisor == 2:
                divisor = 3
            else:
                divisor = divisor + 2
    return factors

if __name__=='__main__':
    main()
