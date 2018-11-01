# first run "chcp 65001" in the command prompt

import string
fname = input("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print('Cannot open file')
    exit()
# putting the senders in a dictionary together with the number of meials they sent
counts = dict()
ntext = ''

# first strip the text of spaces white lines, special charcters
for line in (fhandle):
    line = line.rstrip()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.translate(line.maketrans('','', string.digits))
    line = line.translate(line.maketrans('','', string.whitespace))
    line = line.lower()
    #make new textfile with only charcaters
    ntext = ntext + line
#print(ntext)

tchar = len(ntext)

#count the charcters in a dictionary
for c in ntext:
    counts[c] = counts.get(c,0)+1
#print(counts)


# put the dictionary in a list rverse the order and print the personthat sent the most emails

ml = list()
for key, val in counts.items():
    ml.append((key, val))
ml.sort()
for key, val in ml[:]:
    perc = round((val/tchar)*100,3)
    print(key, perc,'%')
