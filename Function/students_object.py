from generator import generate_students as generate_student_data
from Class import Student
Student = Student.Student


def main():
    x = generate_students(2)
    for keys, values in x.items():
        print(f'{keys}, {values}')


def generate_students(num, additional_info=False):
    student_data = (generate_student_data(num, additional_info))
    students = [Student(**data) for data in student_data]

    master_list = {}
    for student in students:
        last_name = student.name.split(',')[0].strip
        master_list[last_name[0]] = student
    return master_list


if __name__ == "__main__":
    main()
