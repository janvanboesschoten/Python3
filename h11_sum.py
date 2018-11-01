import re
nlist = list()
total = 0
count = 0

fname = input('Enter file name: ')
fhandle = open(fname)
# search all numbers
for line in fhandle:
    line = line.rstrip()
    #mwords = line.split()
    #print(mwords)
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        #print(x)
        nlist.extend(x)
#print(nlist)
for numb in nlist:
    numb = int(numb)
    total = total + numb
    count = count + 1
print (count, total)
