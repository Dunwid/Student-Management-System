from Class import Student
Student = Student.Student

def main():
    bert1 = Student('Malinis, Johnbert', '202210', 'B')

    print(bert1.fullname)
    print(Student.count('B'))

if __name__ == '__main__':
    main()
