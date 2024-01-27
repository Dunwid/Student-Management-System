from tabulate import tabulate
from Class import Student
from Function import students_object
Student = Student.Student
generate_student_data = students_object.generate_students


def main():
    handle_user_input()


def handle_user_input():
    display_menu()
    while True:
        try:
            user_input = input('Enter key: ').upper()
            match user_input:
                case 'C':
                    num_students = int(input('How many students? '))
                    if isinstance(num_students, int):
                        students = generate_student_data(num_students)
                        for _ in students:
                            print(_)
                case 'R':
                    print(Student.data())
                case 'U':
                    pass
                case 'D':
                    print("Saturday")
                case 'S':
                    print("Wednesday")
                case 'O':
                    print("Wednesday")
                case 'X':
                    break
                case _:
                    raise ValueError
        except ValueError:
            print('Invalid command')
    members()


def display_menu():
    table = [['C', 'Create Students List'], ['R', 'Read Students List'],
             ['U', 'Update Students List'], ['D', 'Delete Students List'],
             ['S', 'Save List'], ['X', 'Exit Program'], ['O', 'Options']
             ]
    print("-----------display_menu------------")
    print(tabulate(table, tablefmt="grid"))


def members():
    return print(""""
    STUDENT MANAGEMENT SYSTEM
    BSCS 2B PROJECT

    MEMBERS:
        Malinis, Johnbert
        Mayor, Mark Aaron
        Pula, Henry Luis
        """)


if __name__ == "__main__":
    main()
