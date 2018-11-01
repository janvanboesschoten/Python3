smallest = None
largest = None
while True:
    num = input('Enter number: ')
    if num == 'done':
        break
    else:
        try:
            num = int(num)
        except:
            print('Invalid input')
            continue
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
print('Maximum is', largest)
print('Mimimum is', smallest)
