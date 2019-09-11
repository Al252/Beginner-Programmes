class Interns:
    def __init__(self, name, course, sex, years_of_study_remained):
        self.course = course
        self.sch_yrs = int(years_of_study_remained)
        self.names = name.split(' ')

        if sex == 'M':
            self.name = 'Mr ' + name.split(' ')[-1]
            self.sex = 'Male'
        elif sex == 'F':
            self.name = 'Mrs ' + name.split(' ')[-1]
            self.sex = 'Female'
        else:
            print('Invalid gender response')


    def full_details():
        print(f'Hello {intern.name}. We are glad that you are reading {intern.course}.')
        print(f'{intern.sex}s reportedly find {intern.course} challenging.')
        print(f'For this reason, we are giving you a {intern.sch_yrs}-year scholarship.')
        print(f'We wish we could have helped in your first {4 - intern.sch_yrs} of school.')
        print(f'All the best {intern.names[0]}☺')


intern = Interns(input('Full Name: ').title(), input('Course: ').title(), input('Sex: ').upper(), input('Yrs Left: '))
Interns.full_details()
