fname = input("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print('Cannot open file')
    exit()
# putting the senders in a dictionary together with the number of meials they sent
counts = dict()
for line in (fhandle):
    line = line.rstrip()
    if not line.startswith('From:')  :
        continue
    else:
        words = line.split()
        key = words[1]
        counts[key] = counts.get(key,0) + 1
#print(counts)

# put the dictionary in a list rverse the order and print the personthat sent the most emails
ml = list()
for key, val in counts.items():
    ml.append((val, key))
ml.sort(reverse = True)
for key, val in ml[0:1]:
    print(val, key)
