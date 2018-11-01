fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print(fname, 'cannot be opened')
    quit()
numb = 0
count = 0
for line in fhandle:
    # take out the new line
    line=line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1:
        continue
    else:
        value = float((line[20:26]))
        numb = numb + value
        count = count + 1
print ('Average spam confindence:',numb/count)
