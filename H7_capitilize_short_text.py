fname = input ('Enter a file name: ')
try:
    fhandle = open (fname)
    shout = fhandle.read()
    shout = shout.rstrip()
    print (shout.upper())
except:
    print (fname, 'is not a file')
    quit()
