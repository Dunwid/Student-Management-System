from Class import Student
from Function import generator
generator = generator.generator


def main():
    student = []
    students = []
    for i in range(10):
        student1 = {}
        name, section, student_no = generator(additional_info=True)
        student1['name'] = name
        student1['section'] = section
        student1['student_no'] = student_no
        i += 1
        student.append(student1)

    print(student)


if __name__ == '__main__':
    main()
