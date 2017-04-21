#created by biracruz on 23 May 2012
import sys, os

count = 0

def punch(list, index, value):

    #center
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
    global count
    count = count + 1
    return list

def main():
    input = raw_input()
    l0 = list(input.strip())
    l = []
    for i in l0:
        l.append(eval(i))

     
    value = [1,2,1,3,2,1,0]
    
    i=0
    while i <> 0:
        try:
            index = l.index(value[i])
            l = punch(l, index, value[i])
        except ValueError:
            i = i +1
            pass
    print count