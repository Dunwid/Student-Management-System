from Class import Student
from Function import students_object
Student = Student.Student

def main():
    bert1 = Student('Bert Malinis', 202210612, 'B')

    print(Student.count('B'))


if __name__ == '__main__':
    main()
