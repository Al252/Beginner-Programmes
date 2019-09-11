posibilities = []
faces = [1, 2, 3, 4, 5, 6]
for toss_1 in faces:
    for toss_2 in faces:
        for toss_3 in faces:
            for toss_4 in faces:
                for toss_5 in faces:
                    for toss_6 in faces:
                        posibilities.append((toss_1, toss_2, toss_3, toss_4, toss_5, toss_6))

print('Total Possible Outcomes', len(posibilities))
print('Ranging from', posibilities[0], end = '')
middle = len(posibilities)//2
print(posibilities[middle], end = '')
print('all the way to ', posibilities[-1])
