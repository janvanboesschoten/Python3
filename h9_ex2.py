
fname = input('Enter a file name: ')
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
        if len(words) > 2:
            if words[2] not in counts:
                counts[words[2]] = 1
            else:
                counts[words[2]] += 1
print(counts)
