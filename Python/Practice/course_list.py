def t_func(each, key):
    each = each.split(' ')
    index = 0
    time = []
    t_str = ''
    for word in each:
        if word == key:
            time = each[index + 1:index + 4]
        index += 1
    if time:
        for digit in time:
            t_str += ' ' + digit
        return t_str

def name_only(each):
    n_str = ''
    each = each.split(' ')
    name = each[1:-7]
    for a in name:
        n_str += a + ' '
    return n_str

def c_codes(each):
    c = each.split(' ')[0]
    return c


print('\t\t\t\t\t\t2019/2020 ACADEMIC YEAR')
file = 'C:\\Users\\alber\\Desktop\\Level 300\\General Info\\Courses.txt'
mon = []
tue = []
wed = []
thurs = []
fri = []
time = []

#LINK EACH LINE WITH A DAY OF THE WEEK
with open(file) as courses:
    contents = courses.readlines()
    for line in contents:
        if 'Monday' in line.split(' '):
            mon.append(line)
        elif 'Tuesday' in line.split(' '):
            tue.append(line)
        elif 'Wednesday' in line.split(' '):
            wed.append(line)
        elif 'Thursday' in line.split(' '):
            thurs.append(line)
        elif 'Friday' in line.split(' '):
            fri.append(line)
        else:
            print(f'"{line}" is not linked to any day')


#OUTPUT FOR EACH DAY FOR NON-EMPTY DAY LISTS
if mon:
    key = 'Monday'
    print('\nMondays:', end = '')
    for each in mon:
        print('\n\t' + 'Course: ' + name_only(each).rstrip() + '\n\t' + 'Venue: ' + each.split(' ')[-1] + '\tTime:', end = '')
        print(t_func(each, key))
        print('\tCode: ', end = '')
        print(c_codes(each))
if tue:
    key = 'Tuesday'
    print('\nTuesdays:', end = '')
    for each in tue:
        print('\n\t' + 'Course: ' + name_only(each).rstrip() + '\n\t' + 'Venue: ' + each.split(' ')[-1] + '\tTime:', end = '')
        print(t_func(each, key))
        print('\tCode: ', end = '')
        print(c_codes(each))
if wed:
    key = 'Wednesday'
    print('\nWednesdays:', end = '')
    for each in wed:
        print('\n\t' + 'Course: ' + name_only(each).rstrip() + '\n\t' + 'Venue: ' + each.split(' ')[-1] + '\tTime:', end = '')
        print(t_func(each, key))
        print('\tCode: ', end = '')
        print(c_codes(each))
if thurs:
    key = 'Thursday'
    print('\nThursdays:', end = '')
    for each in thurs:
        print('\n\t' + 'Course: ' + name_only(each).rstrip() + '\n\t' + 'Venue: ' + each.split(' ')[-1] + '\tTime:', end = '')
        print(t_func(each, key))
        print('\tCode: ', end = '')
        print(c_codes(each))
if fri:
    key = 'Friday'
    print('\nFridays:', end = '')
    for each in fri:
        print('\n\t' + 'Course: ' + name_only(each).rstrip() + '\n\t' + 'Venue: ' + each.split(' ')[-1] + '\tTime:', end = '')
        print(t_func(each, key))
        print('\tCode: ', end = '')
        print(c_codes(each))

#CREATE AND PRINT A UNIQUE VENUE-LIST
venues = []
for day in contents:
    venue = (day.split(' ')[-1])
    if venue not in venues:
        venues.append(venue)
venues.sort()
print('\nALL VENUES:')
for each in venues:
    print('\t-' + each.rstrip())

#CREATE AND PRINT A UNIQUE COURSE CODE LIST
print('\nCOURSE CODES:')
course_codes = []
for each in contents:
    each = each.split(' ')
    if each[0] not in course_codes:
        course_codes.append(each[0])
for c in course_codes:
    print('\t-' + c)
