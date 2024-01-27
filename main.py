from Class import Student
Student = Student.Student

def main():
    bert1 = Student('Mark Aaron A. Mayor Jr.', '202210', 'B')

    print(bert1.name)
    print(bert1.fullname)
    print(Student.count_all())

if __name__ == '__main__':
    main()
