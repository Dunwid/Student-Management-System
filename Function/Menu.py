from tabulate import tabulate

def main():
    menu()

def menu():
    headers = ["MENU"]
    table = [['G', 'Generate Students'], ['I', 'Input Students'], ['C', 'From CSV'],
             ['R', 'See Students'], ['U', 'Update Students'], ['D', 'Delete Students']]
    print("----------MENU-----------")
    print(tabulate(table, tablefmt="grid"))
    key = input('Enter key: ')
main()