fname = input('Enter a file name: ')
#fname='mbox-short.txt'
fhandle = open(fname)
count = 0
for line in fhandle:
    line = line.strip()
    # looks for lines that start with from, take the line, split it and returnes the second ietem in the list
    if line.startswith('From'):
        words=line.split()
        print(words[1])
        count = count +1
    else:
        continue
print('There were', count, 'lines in the file with From as the first word')
