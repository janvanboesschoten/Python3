def count(x,y):
    word = str(x)
    y = str(y)
    count = 0
    for letter in word:
        if letter == y:
            count = count + 1
    print (count)
