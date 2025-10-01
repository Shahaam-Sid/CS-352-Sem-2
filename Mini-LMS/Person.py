from Course import CourseList

class Person:
    def __init__(self, name, age, contact, mail):
        self.name = name
        self.age = age
        self.contact = contact
        self.mail = mail
        
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a String')
        value = value.strip()
        if len(value) < 6 or len(value) > 30:
            raise ValueError('Name must contain 6 - 30 Characters')
        if not all((x.isalpha() or x.isspace()) for x in value):
            raise ValueError('Name must only contain Alphabet and spaces')
    
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be an Integer Value')
        if value < 18:
            raise ValueError('Age must be more then 17')
        if value > 100:
            raise ValueError('Invalid Age')
        
        self.__age = value
        
    @property
    def contact(self):
        return self.__contact
    
    @contact.setter
    def contact(self, number):
        if not isinstance(number, str):
            raise TypeError('Contact No. must be a String Value')
        number.strip()
        if any(not x.isdecimal() for x in number):
            raise ValueError('Contact No. must only consist of digits')
        if len(number) != 11:
            raise ValueError('Contact No. must contain 11 digits')
        if not (number[0] == '0' and number[1] == '3'):
            raise ValueError('Incorrect Number Format')
        
        self.__contact = number
        
    @property
    def mail(self):
        return self.__mail
    
    @mail.setter
    def mail(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a String Value")
        value = value.strip()
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        if value.startswith("@") or value.endswith("@"):
            raise ValueError("'@' cannot be in the start or in the end")
        splitted_mail = value.split("@")
        if "." not in splitted_mail[-1]:
            raise ValueError("E-mail must contain .com/.net etc.")
        if len(splitted_mail[0]) < 1 or len(splitted_mail[0]) > 50:
            raise ValueError("Invalid Length")
        
        self.__mail = value
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact}, E-Mail: {self.mail}"
    

class Student(Person):
    def __init__(self, name, age, contact, mail, seat_no, sem, field, courses):
        super().__init__(name, age, contact, mail)
        
        self.seat_no = seat_no
        self.sem = sem
        self.field = field
        self.courses = courses
        
    @property
    def seat_no(self):
        return self.__seat_no
    
    @seat_no.setter
    def seat_no(self, value):
        if not isinstance(value, str):
            raise TypeError('Seat No. must be a String Value')
        value = value.upper()
        if not value.isalnum():
            raise ValueError('Seat No. must only consist of Alphabets and Number')
        if len(value) != 11:
            raise ValueError('Seat No. must consist of 11 Characters')
        if value[0] != 'B':
            raise ValueError('Incorrect Seat No. Format')
        
        self.__seat_no = value
        
    @property
    def sem(self):
        return self.__sem
    
    @sem.setter
    def sem(self, value):
        if not isinstance(value, int):
            raise TypeError('Semester must be an Integer Value')
        if value < 1 or value > 8:
            raise ValueError('Semester must be between 1 - 8')
        
        self.__sem = value
        
    @property
    def field(self):
        return self.__field
    
    @field.setter
    def field(self, value):
        if not isinstance(value, str):
            raise TypeError('Field must be a String Value')
        if value not in {'CS', 'SE', 'AI'}:
            raise ValueError("Invalid Field, Valid option are: CS, SE, AI")
        
        self.__field = value
        
    @property
    def courses(self):
        return self.__courses
    
    @courses.setter
    def courses(self, course_list):
        if not isinstance(course_list, CourseList):
            raise TypeError('Courses must be a CourseList Value')
        
        self.__courses = course_list
        
    def update(self, **attributes):
        for key, value in attributes.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f'Invalid Argument: {key}')
            
    def __str__(self):
        return f"""Name: {self.name}    Age: {self.age}
Seat No: {self.seat_no}    Field: {self.field}
Semester: {self.sem}    Courses: {self.courses}
Contact: {self.contact}    E-Mail: {self.mail}
"""