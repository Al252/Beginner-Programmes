import math


credit_rating = int(input('Credit Rating: '))
price = int(input('Loan Required: '))
if credit_rating >= 70:
    good_credit = True
else:
    good_credit = False
if good_credit:
    down_payment = math.ceil(0.1 * price)
else:
    down_payment = math.ceil(0.2 * price)
msg = f'You are to pay a down payment of £{down_payment}.'
print(msg)
