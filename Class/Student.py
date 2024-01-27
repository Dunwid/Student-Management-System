import re
from tabulate import tabulate
import sys


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

    # Students data
    def to_dict(self):
        return {
            'name': self.name,
            'section': self.section,
            'student_no': self.number,
            'birthday': self.birthday,
            'address': self.address,
            'email': self.email,
            'phone_no': self.phone_number
        }
    
    @property
    def name(self):
        return self._name

    # Check if the name was properly formatted into Lastname, Name format
    @name.setter
    def name(self, name):
        name = name.strip()
        if matches := re.match(r"^([A-z][a-z ]+), ([A-z][A-za-z ]+) ?([A-Z].?)? ?(Jr.?|Sr.?)?$", name):
            self._name = name
        elif matches := re.match(r"^([A-Z][A-za-z ]+) ([A-Z].)? ([A-z][a-z ]+) ?(Jr.?|Sr.?)?$", name):
            if matches.group(2) and matches.group(4):
                self._name = "{}, {} {}, {}".format(matches.group(3).strip(), matches.group(1),
                                                    matches.group(2), matches.group(4))
            elif matches.group(4):
                self._name = "{}, {} , {}".format(matches.group(3).strip(), matches.group(1), matches.group(4))
            elif matches.group(2):
                self._name = "{}, {} {}".format(matches.group(3).strip(), matches.group(1), matches.group(2))
        else:
            sys.exit('Invalid name format')

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
        if matches := re.match(r"^([A-za-z ]+), ([A-za-z ]+).?,? ?(Jr.?|Sr.?)?$", self.name):
            if matches.group(3):
                return "{} {} {}".format(matches.group(2), matches.group(1), matches.group(3))
            else:
                return "{} {}".format(matches.group(2), matches.group(1))
        else:
            sys.exit('Name error!')

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
