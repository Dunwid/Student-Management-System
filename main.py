from Class import Student
from Function import students_object

Student = Student.Student
generate_student_data = students_object.generate_students


def main():
    students = generate_student_data(3)
    for names, info in students.items():
        print(f"Last name: {names}")
        print(f"INFORMATIONS: {info}")

    print(Student.data())


if __name__ == '__main__':
    main()
