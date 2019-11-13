#https://www.hackerrank.com/challenges/ctci-ransom-note/problem

from collections import Counter

def ransom_note(magazine, ransom):
    magazine_d = Counter(magazine)#{word: magazine.count(word) for word in magazine}
    for ransom_word in ransom:
        if magazine_d.get(ransom_word):
            magazine_d[ransom_word] = magazine_d[ransom_word] - 1
            if magazine_d[ransom_word] == 0:
                del magazine_d[ransom_word]
        else:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
