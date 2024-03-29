import re
from tabulate import tabulate
import sys
import pickle


class Student:
    # Class dictionary to store all student objects
    database = {}

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

        self.database[int(self.number)] = self.to_dict()
        self.save_students()

    def __str__(self):
        return "Hello {}! Student No.{} from BSCS 2{}".format(self.fullname, self.number, self.section.upper())

    # Students data
    def to_dict(self):
        return {
            'name': self.name,
            'section': self.section,
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
        elif matches := re.match(r"^([A-Z][A-za-z ]+) ?([A-Z].)? ([A-z][a-z ]+) ?(Jr.?|Sr.?)?$", name):
            if matches.group(2) and matches.group(4):
                self._name = "{}, {} {}, {}".format(matches.group(3).strip(), matches.group(1),
                                                    matches.group(2), matches.group(4))
            elif matches.group(4):
                self._name = "{}, {} , {}".format(matches.group(3).strip(), matches.group(1), matches.group(4))
            elif matches.group(2):
                self._name = "{}, {} {}".format(matches.group(3).strip(), matches.group(1), matches.group(2))
            else:
                self._name = "{}, {}".format(matches.group(3).strip(), matches.group(1))
        else:
            raise ValueError('Invalid name format')

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
        self.SECTIONS[self.section].append(self.fullname)

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
        section_students = []
        section = section.upper()
        if section not in cls.SECTIONS:
            raise ValueError('Invalid Section'.upper())
        for number, infos in cls.database.items():
            for k, v in infos.items():
                if v == section:
                    name = cls.database[number]['name']
                    name = name.strip()
                    if matches := re.match(r"^([A-za-z ]+), ([A-za-z ]+).?,? ?(Jr.?|Sr.?)?$", name):
                        if matches.group(3):
                            name = "{} {} {}".format(matches.group(2), matches.group(1), matches.group(3))
                        else:
                            name = "{} {}".format(matches.group(2), matches.group(1))
                    section_students.append(name)
        i = 1
        table = []
        for student in section_students:
            countings = []
            countings.append(i)
            countings.append(student)
            table.append(countings)
            i += 1
        count = ['TOTAL COUNT', f'{len(section_students)}']
        table.append(count)
        return tabulate(table, headers=[f'SECTION {section}', 'STUDENT NAMES'], tablefmt="grid")
        # return 'Section {} TOTAL COUNT: {}'.format(section, len(cls.SECTIONS[section]))

    # returns the number of Overall Students
    @classmethod
    def count_all(cls):
        a = len(cls.SECTIONS['A'])
        b = len(cls.SECTIONS['B'])
        c = len(cls.SECTIONS['C'])
        overall = a + b + c
        table = [['Section A', a], ['Section B', b], ['Section C', c], ['Overall', overall]]
        headers = ['Section', 'Number of\nStudents']
        return tabulate(table, headers, tablefmt='grid', maxcolwidths=[9, 1])

    @classmethod
    def data(cls):
        table = []
        sorted_dict = dict(sorted(cls.database.items()))
        for number, infos in sorted_dict.items():
            combined = []
            info = []
            for k, v in infos.items():
                k = k.title()
                v.title()
                info.append(f'{k}: {v}')
            combined.append(number)
            info = ' '.join(map(str, info))
            combined.append(info)
            table.append(combined)

        return tabulate(table, headers=['Student Number', 'INFORMATIONS'], tablefmt='pretty', stralign="left")
    # return tabulate([[k, v] for k, v in sorted_dict.items()], headers=['Student Number', 'INFORMATIONS'], tablefmt='pretty')

    # Save database
    @classmethod
    def save_students(cls):
        with open('student_data.pkl', 'wb') as file:
            pickle.dump(cls.database, file)

    @classmethod
    def load_students(cls):
        try:
            with open('student_file.pkl', 'rb') as f:
                return pickle.load(f)  # deserialize using load()
        except FileNotFoundError:
            print('File does not exist')

    @classmethod
    def remove(cls, number):
        cls.database.pop(number, None)

    @classmethod
    def update(cls, name, change, to):
        for number, info in cls.database.items():
            last_name = cls.database[number]['name'].split(',')
            if last_name[0] == name:
                cls.database[number][change] = to
