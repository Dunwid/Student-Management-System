from faker import Faker

import random
import sys

fake = Faker()


def main():
    print(generate_students(1, additional_info=True))


# Generate the lists of Students
# Returns a list
# Asks for an int argument, additional_info is optional
# Will limit num_students into 20 to avoid crash
# Provide additional_info=True, if personal information was needed.
def generate_students(num_students, additional_info=False):
    if isinstance(num_students, int) and num_students <= 20:
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
    # Exits if num_students is invalid

    else:
        sys.exit('Please provide the number of students.')


# Generate Students data
def generate_student_info(additional_info=False):
    # Provide personal info, if additional_info = True
    # If not, proceeds with school information only
    if additional_info:
        sections = ['A', 'B', 'C']
        name = fake.name()
        section = random.choice(sections)
        student_no = '202210' + str(random.randint(000, 600)).zfill(3)
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=22).strftime('%m/%d/%Y')
        address = fake.address()
        email = fake.email()
        phone_number = f'09{fake.msisdn()[4:]}'
        return name, section, student_no, birthday, address, email, phone_number
    else:
        sections = ['A', 'B', 'C']
        name = fake.name()
        section = random.choice(sections)
        student_no = '2022' + str(random.randint(00000, 10000)).zfill(5)
        return name, section, student_no


if __name__ == "__main__":
    main()
