#created by biracruz on 23 May 2012

lines= int(raw_input())
list = []
for x in range(lines):
    list.append(int(raw_input()))
for y in list:
    if (y % 4) == 0 or (y % 4) == 1:
        print "YES"
    else:
        print "NO"