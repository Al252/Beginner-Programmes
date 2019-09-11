input1 = input('First Array(seperate numbers with ","): ').split(',')
input2 = input('Second Array(seperate numbers with ","): ').split(',')

nums1 = []
nums2 = []

for a in input1:
    int(a)
    nums1.append(a)
for b in input2:
    int(b)
    nums2.append(b)

def mean(first, second):
    u = first + second
    div = len(u)
    total = 0
    for item in u:
        total += int(item)
    return total/div

print(mean(nums1, nums2))
