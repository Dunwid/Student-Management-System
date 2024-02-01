from tabulate import tabulate
from Class import Student
from Function import students_object
Student = Student.Student
generate_student_data = students_object.generate_students


def main():
    handle_user_input()


def handle_user_input():
    display_menu()
    students = ()
    while True:
        try:
            user_input = input('ENTER KEY: ').upper()
            match user_input:
                case 'C':
                    num_students = int(input('How many students? '))
                    if isinstance(num_students, int):
                        students = generate_student_data(num_students)
                case 'R':
                    print(Student.data())
                case 'U':
                    if len(students) > 0:
                        tries = 0
                        while True:
                            try:
                                name = input("Enter last name: ").title()
                                if name in students:
                                    tries = 0
                                    change = input("Change: ").lower()
                                    if change in ['name', 'number', 'section', 'birthday', 'age', 'address', 'email', 'phone_number']:
                                        value = input(f"Enter new {change}: ")
                                        Student.update(name, change, value)
                                        break
                                    else:
                                        raise ValueError
                                else:
                                    raise ValueError
                            except ValueError:
                                if tries == 2:
                                    print('LIMIT REACHED')
                                    break
                                else:
                                    tries += 1
                                    if tries == 2:
                                        print(f'Name not recognized. {3 - tries} chance left'.upper())
                                    else:
                                        print(f'Name not recognized. {3 - tries} chances left'.upper())
                                    pass
                    else:
                        print('EMPTY DATABASE')
                case 'D':
                    number = int(input("Enter Student Number: "))
                    Student.remove(number)
                # case 'S':
                #     print("Wednesday")
                case 'O':
                    display_options()
                    while True:
                        user_input = input('ENTER KEY: ').upper()
                        try:
                            match user_input:
                                case 'V':
                                    print(Student.count_all())
                                case 'Z':
                                    section = input('COUNT SECTION: ').upper()
                                    print(Student.count(section))
                                case 'G':
                                    for _ in students:
                                        print(_)
                                case 'X':
                                    break
                                case '_':
                                    raise ValueError
                        except ValueError:
                            print('INVALID COMMAND!')
                case 'X':
                    break
                case _:
                    raise ValueError
        except ValueError:
            print('INVALID COMMAND!')
        except EOFError:
            break
    members()


def display_menu():
    # table = [['C', 'Create Students List'], ['R', 'Read Students List'],
    #          ['U', 'Update Students List'], ['D', 'Delete Students List'],
    #          ['S', 'Save List'], ['X', 'Exit Program'], ['O', 'Options']
    #          ]
    table = [['C', 'Create Students List'], ['R', 'Read Students List'],
             ['U', 'Update Students List'], ['D', 'Delete Students List'],
             ['X', 'Exit Program'], ['O', 'Options']
             ]

    print("-----------display_menu------------")
    print(tabulate(table, tablefmt="grid"))

def display_options():
    table = [['V', 'View all sections'], ['Z', 'View Students in Section'], ['G', 'Greet all'], ['X', 'Exit Options']]
    print("-----------OPTIONS------------")
    print(tabulate(table, headers=['OPTIONS'], tablefmt="grid"))


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
