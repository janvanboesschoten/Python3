
def computepay(h,r):
    hours = float(h)
    rate = float(r)
    if hours > 40:
        xtrhours = hours-40
        hours = hours-xtrhours
        pay = (hours*rate) + (xtrhours*(rate*1.5))
        return pay
    else:
        pay = float(hours)*float(rate)
        return pay


h = input('Enter your hours: ')
r = input('Enter your rate: ')
print(computepay(h,r))
