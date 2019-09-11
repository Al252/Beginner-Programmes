def pal(word):
    word = word.lower()
    arr = []
    comp = []
    rword = []
    for letter in word:
        arr.append(letter)
        comp.append(letter)

    amt = len(arr)
    for each in range(amt):
        rword.append(arr[-1])
        arr.pop(-1)
    if rword == comp:
        msg = True
    else:
        msg = False
    return msg
print(pal(input('Word: ')))