import re
fname = 'mbox.txt'
count = 0
# find the regula expression from input
ename = input('Enter a regular expression: ')
#print(ename)
#print(type(ename))
fhandle = open(fname)
for line in fhandle:
    #line = line.strip()
    x = re.findall(ename, line)
    if len(x) > 0:
        #print(x)
        count = count + 1
print(fname, 'had', count, 'lines that matches', ename)
