#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

#7 of 9
# def array_left_rotation(a, n, k):
#     new = []
#     ref = a
#     for i in range(k):        
#         new = ref[1:]
#         new.append(ref[0])
#         ref = new
#     return new

# n, k = map(int, raw_input().strip().split(' '))
# a = map(int, raw_input().strip().split(' '))
# answer = array_left_rotation(a, n, k);
# print ' '.join(map(str,answer))

#9 of 9 :)
def array_left_rotation(a, n, k):
    new = [0] * n
    positive_increment = n - k
    for i in range(n):
        if i < k:
            new[i + positive_increment] = a[i]
        else:
            new[i - k] = a[i]       
    return new

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))