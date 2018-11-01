
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
        key = words[1]
        counts[key] = counts.get(key,0) + 1
#print(counts)
largest = None
#smallest = None
#lst = list(counts.keys())
lst2 = list(counts.values())
for numb in lst2:
    if largest is None or numb > largest:
        largest = numb
for numb in counts:
    if counts[numb] == largest:
        print(key, count[key])
#    if smallest is None or numb < smallest:
#        smallest = numb
print(largest)
