import re
from tabulate import tabulate


class Student:

    # Segregate Students to their designated Section
    SECTIONS = {'A': [], 'B': [], 'C': []}

    def __init__(self, name, number, section, birthday='', age='', address='', email='', phone_number=''):
        self.name = name
        self.number = number
        self.section = section
        self.birthday = birthday
        self.age = age
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return "Hello {}! Student No.{} from BSCS 2{}".format(self.fullname, self.number, self.section.upper())

    @property
    def name(self):
        return self._name

    # Check if the name was properly formatted into Lastname, Name format
    @name.setter
    def name(self, name):
        name = name.strip()
        matches = re.search(r"^([A-Za-z -]+(?:\s[A-Za-z -]+)*), ([A-Za-z -]+(?:\s[A-Za-z -]+)*)\s*([A-Za-z])?$", name)
        if matches:
            last_name = matches.group(1)
            first_name = matches.group(2)
            middle_initial = matches.group(3) if matches.group(3) else ''
            self._name = f"{last_name}, {first_name} {middle_initial}".strip()
        else:
            raise ValueError('Invalid Name Format')

    @property
    def section(self):
        return self._section

    # Check if the section was valid
    # Name then putted into the section list
    @section.setter
    def section(self, section):
        section = section.upper()
        if section not in ['A', 'B', 'C']:
            raise ValueError('Invalid Section')
        self._section = section
        self.SECTIONS[self.section] = [self.fullname]

    # Prints name in firstname lastname format
    @property
    def fullname(self):
        last, first = self.name.split(', ')
        return f"{first} {last}"

    # Prints personal information
    @property
    def additional_info(self):
        return """Age: {}
Address: {}
Email: {}
Phone Number: {}""".format(self.age, self.address, self.email, self.phone_number)

    # returns the number of SECTIONS
    @classmethod
    def all_SECTIONS(cls):
        return len(cls.SECTIONS)

    # returns the number of student per section
    @classmethod
    def count(cls, section):
        section = section.upper()
        if section not in ['A', 'B', 'C']:
            raise ValueError('Invalid Section')
        cls.section = section
        headcount = len(Student.SECTIONS[cls.section])
        return headcount

    # returns the number of Overall Students
    @classmethod
    def count_all(cls):
        tabulate.PRESERVE_WHITESPACE = True
        a = len(Student.SECTIONS['A'])
        b = len(Student.SECTIONS['B'])
        c = len(Student.SECTIONS['C'])
        overall = a + b + c
        table = [['Section A', a], ['Section B', b], ['Section C', c], ['Overall', overall]]
        headers = ['Section', 'Number of\nStudents']
        return tabulate(table, headers, tablefmt='grid', maxcolwidths=[9, 1])
