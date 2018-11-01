
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file:' ,fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    else:
        words = line.split()
        value = words[1]
        counts[value] = counts.get(value,0)+1
#worddict[word] = worddict.get(word,0) + 1
print(counts)
