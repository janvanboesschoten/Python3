txt = 'but soft what light in yonder window breaks'
words= txt.split()
print (words)
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
print(t)

res = list()
for length, word in t:
    res.append(word)
print(res)


d ={'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items():
    l.append((val,key))

print(l)
l.sort(reverse=True)
print(l)
