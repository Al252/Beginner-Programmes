import datetime

current = datetime.date.today()
usrdline = input('Deadline(DD/MM/YYYY): ')
dline = datetime.datetime.strptime(usrdline, '%d/%m/%Y').date()
days = (dline - current).days
if days == 0:
    print('Project is due today!!!')
elif days <= 0:
    if days == -1:
        print('Deadline was yesterday.')
    elif days < -1:
        print(f'Deadline was {abs(days)} days ago.')
elif days < 7:
    print(f'You have {days} days more.')
elif (days>7) and (days<365):
    print(f'You have {int((days - (days%7))/7)} weeks and {days%7} days more.')
elif days > 365:
    print('You have over a year remaining.')
