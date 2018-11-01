import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    #takes white space away at the end
    line = line.rstrip()
    #takes punctuation out of the string
    line = line.translate(line.maketrans('', '', string.punctuation))
    #caps out the strings
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
#print (counts)
        #worddict[word] = worddict.get(word,0) + 1
    #print(worddict)
    lst = list(counts.keys())
    lst.sort()
    #print(lst)
    for word in counts:
        print(word, counts[word])
