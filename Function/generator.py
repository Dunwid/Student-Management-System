from faker import Faker
import random
import sys

fake = Faker()

def main():
    generate_students(2)


# Generate the list of students on list
def generate_students(num_students, additional_info=False):
    if isinstance(num_students, int):
        students = []
        if additional_info:
            for _ in range(num_students):
                student_info = generate_student_info(additional_info=True)
                student_info_keys = ['name', 'section', 'student_no', 'birthday', 'address', 'email', 'phone_no']
                student_data = {key: value for key, value in zip(student_info_keys, student_info)}
                students.append(student_data)
        else:
            for _ in range(num_students):
                student_info = generate_student_info()
                student_info_keys = ['name', 'section', 'student_number']
                student_data = {key: value for key, value in zip(student_info_keys, student_info)}
                students.append(student_data)
        return students

    else:
        sys.exit('Please provide the number of students.')


# Generate names, student,
def generate_student_info(additional_info=False):
    if additional_info:
        print('hey!')
    else:
        sections = ['A', 'B', 'C']
        name = fake.name()
        section = random.choice(sections)
        student_no = '2022' + str(random.randint(00000, 10000)).zfill(4)
        return name, section, student_no

if __name__ == "__main__":
    main()
