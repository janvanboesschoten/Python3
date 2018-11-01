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
    if not line.startswith('From')  :
        continue
    else:
        words = line.split()
        if len(words) < 3:
            continue
        else:
            #print(words)
            time = words[5]
            hour = time.split(':')
            key = hour[0]
            #print(key)
            counts[key] = counts.get(key,0) + 1
#print(counts)

# put the dictionary in a list rverse the order and print the personthat sent the most emails
ml = list()
for key, val in counts.items():
    ml.append((key, val))
ml.sort()
for key, val in ml[:]:
    print(key, val)
