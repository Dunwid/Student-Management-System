from faker import Faker
import random
fake = Faker()

# Generate the list of students on list
def generate(num, additional_info=False):
    add = additional_info
    student = []
    students = []
    if num is int:
        if add:
            generator(additional_info=True)
        else:
            for i in range(num):
                student1 = {}
                name, section, student_no = generator()
                student1['name'] = name
                student1['section'] = section
                student1['student_no'] = student_no
                i += 1
                student.append(student1)
    else:
        raise ValueError('Enter the Number of Students')

# Generate names, student,
def generator(additional_info=False):
    if additional_info:
        print('hey!')
    else:
        sections = ['A', 'B', 'C']
        name = fake.name()
        section = random.choice(sections)
        student_no = random.randint(00000, 10000)
        student_no = '2022' + str(student_no)
        return name, section, student_no
