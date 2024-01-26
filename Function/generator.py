from faker import Faker
import random
import sys
fake = Faker()

def main():
    generate(2)

# Generate the list of students on list
def generate(num, additional_info=False):
    add = additional_info
    students = []
    if type(num) is int:
        if add:
            name, section, student_no, birthday, address, email, phone_no = generator(additional_info=True)
        else:
            for i in range(num):
                student_info = generator()
                info_keys = ['name', 'section', 'student_number']
                generate_list = {key: value for key, value in zip(info_keys, student_info)}
                students.append(generate_list)
                i += 1
        return students

    else:
        sys.exit('Enter how many students')

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

main()