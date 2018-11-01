import re
count = 0
nlist = list()
total = 0
# find the regula expression from input
fname = input('Enter filename: ')
fhandle = open(fname)
for line in fhandle:
    #line = line.strip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        nlist.extend(x)
        count = count + 1
for numb in nlist:
    numb = int(numb)
    total = total + numb
print(count, total, 'avarage =', format(float(total/count), '.7f'))
