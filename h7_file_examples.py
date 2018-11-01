
fhand=open('mbox-short.txt')
count=0
for line in fhand:
    count = count+1
print('Line count:', count)

fband=open('mbox-short.txt')
inp = fband.read()
print(len(inp))
print(inp[:20])

fband=open('mbox-short.txt')
print(len(fband.read()))
print(len(fband.read()))
print(len(fband.read()))



fhand2 = open('mbox-short.txt')
for line in fhand2:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print (line)

fhand3 = open('mbox-short.txt')
for line in fhand3:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)

fname = input('Enter the file name: ')
try:
    fhand4 = open (fname)
except:
    print ('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand4:
    if line.startswith('Subject:'):
        count = count + 1
print('There where', count, 'subject lines in', fname)
