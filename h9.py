eng2sp = dict()
eng2sp ={'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(len(eng2sp))
sleutels = list(eng2sp.keys())
print(sleutels)
vals = list(eng2sp.values())
print(vals)

fhandle = open('words.txt')
wordfile = []
worddict = dict()
for line in fhandle:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in wordfile:
            wordfile.append(word)
            worddict[word] = 1
        else:
            worddict[word] +=1 #worddict[word] = worddict[word] + 1
    print(wordfile)
    print(worddict)
