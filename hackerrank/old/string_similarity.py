#created by biracruz on 23 May 2012

def main():
	cases = int(raw_input())
	results = []
	while ((1 <= cases) and (cases <=  10)):
		word = raw_input()
		if (len(word)>100000):
			break
		else:
			count = 0
			for i in xrange(len(word)):
				sufixe = word[i:]
				position = 0
				while position < len(sufixe):
					if sufixe[position] == word[position]:
						count = count + 1
						position = position +1
					else:
						break 
			results.append(count)
			cases = cases - 1

	for r in results:
		print r
 
if __name__ == '__main__':
    main()