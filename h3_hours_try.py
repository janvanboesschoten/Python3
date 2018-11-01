hours = input('Enter the hour\n')
try:
    hours = float(hours)
except:
    hours = input('Error please enter numeric input\n')

rate = input('Enter your rate per hour?\n')
try:
    rate = float(rate)
except:
    rate = input('Error please enter numeric input\n')
