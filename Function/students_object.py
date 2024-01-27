from generator import generate_students as generate
from Class import Student
Student = Student.Student


def main():
    x = generate_students(2)
    for keys, values in x.items():
        print(f'{keys}, {values}')

def generate_students(num, additional_info=False):
    masterlist = {}
    student_data = {}
    student_data = (generate(num, additional_info))
    number_of_students = len(student_data)
    students = [Student(**data) for data in student_data]

    for student in students:
        student_lastname = student.name.split(',')
        masterlist[student_lastname[0]] = student

    return masterlist


if __name__ == "__main__":
    main()