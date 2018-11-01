count = 0
total = 0
average = 0
while True:
    numb = input('Enter number: ')
    if numb == 'done':
        print(total, count, average)
        break
    else:
        try:
            numb = float(numb)
            count = count + 1
            total = total + numb
            average = total/count
        except:
            print('Invalid input')
