fname = input('Enter the file name: ')
if fname == "na na boo boo":
    print(fname.upper(), 'TO YOU - You have been punk\'d')
else:
    try:
        fhandle = open(fname)
    except:
        print('File cannot be opened:', fname)
        quit()
    count = 0
    for line in fhandle:
        if line.find('Subject:') == -1:
            continue
        else:
            count = count + 1
    print ('There are',count,'subject lines in', fname)
