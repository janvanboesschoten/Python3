fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file:' ,fname)
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    else:
        #print (line)
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1
        #if word not in counts:
        #    counts[word] = 1
        #else:
        #    counts[word] = counts[word] +1
            #worddict[word] = worddict.get(word,0) + 1

#print(counts)
#find largest
largest = None
#lst = list(counts.keys())
lst2 = list(counts.values())
for numb in lst2:
    if largest is None or numb > largest:
        largest = numb
#print(largest)
for numb in counts:
    if counts[numb] == largest:
        print(numb, counts[numb])
