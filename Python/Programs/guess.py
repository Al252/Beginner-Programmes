import random

print("I'm thinking of a single digit number🤔\nWanna Guess?")
secrete_num = random.randint(0, 9)
attempts = 0
attempt_limit = 5
retry = True
while (attempts < attempt_limit) and retry == True:
    print('Remaining Lives: ' + '*' * (attempt_limit - attempts))
    guess = int(input("Guess: "))
    if guess == secrete_num:
        msg = "You win🎉"
        again = input('Play Again? (y/n)').lower()
        if again == 'y':
            retry == True
        else:
            retry == False
    else:
        msg = f'Try again'
    print(msg.upper())
    attempts += 1
else:
    msg = f"Sorry you're out of lives☠\nTry again next time.\nI was thinking of {secrete_num}🤷‍♂️"
    again = input('Retry? (y/n)').lower()
    if again == y:
        retry == True
    else:
        retry == False

print(msg.title())
