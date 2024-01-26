import re
from tabulate import tabulate


class Student:

    # Segregate Students to their designated Section
    sections = {'A': [], 'B': [], 'C': []}

    def __init__(self, name, number, section, age='', address='', email='', phone_number=''):
        self.name = name
        self.number = number
        self.section = section
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
        matches = re.search(r"^([A-Za-z -]+), ([A-Za-z -.]+)$", name)
        if matches:
            self._name = name
        else:
            ...

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
        Student.sections[self.section] = [self.fullname]

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

    # returns the number of sections
    @classmethod
    def all_sections(cls):
        return len(Student.sections)

    # returns the number of student per section
    @classmethod
    def count(cls, section):
        section = section.upper()
        if section not in ['A', 'B', 'C']:
            raise ValueError('Invalid Section')
        cls.section = section
        headcount = len(Student.sections[cls.section])
        return headcount

    # returns the number of Overall Students
    @classmethod
    def count_all(cls):
        tabulate.PRESERVE_WHITESPACE = True
        a = len(Student.sections['A'])
        b = len(Student.sections['B'])
        c = len(Student.sections['C'])
        overall = a + b + c
        table = [['Section A', a], ['Section B', b], ['Section C', c], ['Overall', overall]]
        headers = ['Section', 'Number of\nStudents']
        return tabulate(table, headers, tablefmt='grid', maxcolwidths=[9, 1])
