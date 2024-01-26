from faker import Faker
import random
fake = Faker()


def generator():
    sections = ['A', 'B', 'C']
    name = fake.name()
    section = random.choice(sections)
    student_no = random.randint(00000, 10000)
    student_no = '2022' + str(student_no)
    return name, section, student_no