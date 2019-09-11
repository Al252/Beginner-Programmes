words = []
details = {
    "phone": input('Phone: ')
}
for number in details.get("phone"):
    if number == '+':
        words.append("Plus")
    elif number == '0':
        words.append("Zero")
    elif number == '1':
        words.append("One")
    elif number == '2':
        words.append("Two")
    elif number == '3':
        words.append("Three")
    elif number == '4':
        words.append("Four")
    elif number == '5':
        words.append("Five")
    elif number == '6':
        words.append("Six")
    elif number == '7':
        words.append("Seven")
    elif number == '8':
        words.append("Eight")
    elif number == '9':
        words.append("Nine")
    else:
        print('Invalid Response')
        break
for word in words:
    print(word)
