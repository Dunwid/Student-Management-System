from tabulate import tabulate


def main():
    enter_key()


def enter_key():
    menu()
    while True:
        try:
            button = input('Enter key: ').upper()
            match button:
                case 'C':
                    print("Monday")
                case 'R':
                    print("Thursday")
                case 'U':
                    print("Friday")
                case 'D':
                    print("Saturday")
                case 'S':
                    print("Wednesday")
                case 'X':
                    break
                case _:
                    raise ValueError
        except ValueError:
            print('Invalid KEY')
    members()


def menu():
    table = [['G', 'Generate Students'], ['I', 'Input Students'], ['S', 'Save'],
             ['R', 'See Students'], ['U', 'Update Students'], ['D', 'Delete Students'],
             ['X', 'Exit Program']
             ]
    print("----------MENU-----------")
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
