from generator import generate_students as generate
from Class import Student
Student = Student.Student


def main():
    print(generate_students(2))


def generate_students(num, additional_info=False):
    students = {}
    students_data = generate(num)
    number_of_students = len(students_data)
    for _ in range(number_of_students):
        ...

    return students_data



if __name__ == "__main__":
    main()