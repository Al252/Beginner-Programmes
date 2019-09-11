word = input('Enter word: ')
arr = ['a']
rword = ''
for letter in word:
    print(letter)

arr = arr.sort(reverse=True)
print(arr)


if rword == word:
    print(f'{word} is a Palindrome.')
else:
    print(f'{word} is not a Palindrome')