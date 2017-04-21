#Created by biracruz on 23 May 2012.

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys

def main():
    
    smallest = -1
    start = 2520
    final = 6040
    try:
        while(True):
            for n in range(start,final,10):
                if divisibleByAll(n):
                    smallest = n
                    break
            if smallest<>-1:
                break
            else:
                start = start * 2
                final = final * 2
            print 'FINAL=%d' % final
        print 'SMALLEST=%d' % smallest    
    except MemoryError:
        print 'error, final number = %d' % final 
        
def divisibleByAll(number):
    for i in range(20,0,-1):
        if number%i:
            return False
    return True


if __name__=='__main__':
    main()
