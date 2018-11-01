lvalue = []
while True:
    numb = input('Enter number: ')
    if numb == 'done':
        print('Maximum:', max(lvalue))
        print('Minimum:', min(lvalue))
        break
    else:
        try:
            numb = float(numb)
            lvalue.append(numb)
            #print(lvalue, type(lvalue))
        except:
            print('Invalid input')
