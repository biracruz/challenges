#created by biracruz on 23 May 2012

import sys
input = raw_input()
count = 0
list = list(int(var) for var in input.strip())
value = 1
while value <= 3:
    try:
        index = list.index(value)
        list[index]  = list[index] - value
        #right
        if index + 1 < len(list):
            if list[index +1] - value < 0:
                list[index+1] = 0
            else:
                list[index+1] = list[index + 1] - value
        #left
        if index - 1 >= 0:
            if list[index-1] - value < 0:
                list[index-1] = 0
            else:
                list[index-1] = list[index -1] - value
        count = count + 1
    except ValueError:
        value = value + 1
        pass
print count