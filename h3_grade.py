score = input('Enter score\n')
try:
    grade = float(score)
    if grade < 0.0 or grade > 1.0:
        print('Bad Score')
    elif grade >= 0.9 and grade <= 1.0:
        print('A')
    elif grade >= 0.8 and grade < 0.9:
        print('B')
    elif grade >= 0.7 and grade < 0.8:
        print('C')
    elif grade >= 0.6 and grade < 0.7:
        print('D')
    elif grade >= 0.0 and grade < 0.6:
        print('F')
except:
    print('Bad Score')
