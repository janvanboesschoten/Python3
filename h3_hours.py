hours = input('Enter the hours you worked\n')
hours = float(hours)
rate = input('Enter your rate per hour?\n')
rate = float(rate)

if hours > 40:
    xtrhours = hours-40
    hours = hours-xtrhours
    pay = (hours*rate) + (xtrhours*(rate*1.5))
    print('You get paid:',pay)
else:
    pay = float(hours)*float(rate)
    print('You get paid:', pay)
