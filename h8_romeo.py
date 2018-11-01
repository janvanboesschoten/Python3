fname = input('Enter file: ')
#fname = 'romeo.txt'
fhandle = open(fname)
twords = []
# turn every line in a list of words and check of the words in the list exists in the total list
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for i in words:
        if i not in twords:
            twords.append(i)
twords.sort()
print (twords)
