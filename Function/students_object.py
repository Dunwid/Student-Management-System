from generator import generate_students as generate
from Class import Student
Student = Student.Student


def main():
    print(generate_students(2))


def generate_students(num, additional_info=False):
    student_data = {}
    student_data = (generate(num, additional_info))
    number_of_students = len(student_data)
    print(student_data)
    students = [Student(**data) for data in student_data]

    for student in students:
        print(student)

    # for _ in range(number_of_students):
    #     ...
    #
    # return students_data



if __name__ == "__main__":
    main()