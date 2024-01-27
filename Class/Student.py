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
        def format_name(input_name):
            # Regex pattern for "First MiddleInitial. Last Suffix" format
            pattern1 = r"^([A-Za-z]+)\s([A-Za-z])\.\s([A-Za-z]+)\s([A-Za-z]+)$"

            # Regex pattern for "Last, First MiddleInitial. Suffix" format
            pattern2 = r"^([A-Za-z]+),\s([A-Za-z]+)\s([A-Za-z])\.\s([A-Za-z]+)$"

            match1 = re.match(pattern1, input_name)
            match2 = re.match(pattern2, input_name)

            if match1:
                last_name, first_name, middle_initial, suffix = match1.groups()
                return f"{last_name}, {first_name} {middle_initial}, {suffix}"
            elif match2:
                last_name, first_name, middle_initial, suffix = match2.groups()
                return f"{last_name}, {first_name} {middle_initial}, {suffix}"
            else:
                raise ValueError('Invalid input format')

        name = name.strip()
        formatted_name = format_name(name)
        self._name = formatted_name

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
    def all_sections(cls):
        return len(cls.SECTIONS)

    # returns the number of student per section
    @classmethod
    def count(cls, section):
        section = section.upper()
        if section not in cls.SECTIONS:
            raise ValueError('Invalid Section')
        return 'Number of students in Section {}: {}'.format(section, len(cls.SECTIONS[section]))

    # returns the number of Overall Students
    @classmethod
    def count_all(cls):
        a = len(Student.SECTIONS['A'])
        b = len(Student.SECTIONS['B'])
        c = len(Student.SECTIONS['C'])
        overall = a + b + c
        table = [['Section A', a], ['Section B', b], ['Section C', c], ['Overall', overall]]
        headers = ['Section', 'Number of\nStudents']
        return tabulate(table, headers, tablefmt='grid', maxcolwidths=[9, 1])
