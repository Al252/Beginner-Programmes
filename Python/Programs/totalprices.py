price = input('NB: Seperate prices with [,] only\nPrices: ').split(',')
total = int()
for item in price:
    item = int(item)
    total += item
print(f'TOTAL: {total}')
