from PersonLists import Faculty

class Course:
    
    attributes = "course_id, course_name, course_book, credit_hours, semester, is_optional, teachers"
    
    def __init__(self, course_id, course_name, course_book, credit_hours, semester, is_optional, teachers):
        self.course_id = course_id
        self.course_name = course_name
        self.course_book = course_book
        self.credit_hours = credit_hours
        self.semester = semester
        self.is_optional = is_optional
        self.teachers = teachers
        
    @property
    def course_id(self):
        return self.__course_id
    
    @course_id.setter
    def course_id(self, value):
        if not isinstance(value, str):
            raise TypeError('Course ID must be a String Value')
        value.strip()
        if len(value) != 5:
            raise ValueError('Course ID must be 5 Characters')
        if not value.isalnum():
            raise ValueError('Course ID must only contain Alphabet and Numbers')
        
        self.__course_id = value
        
    @property
    def course_name(self):
        return self.__course_name
    
    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Course Name must be a String Value')
        value.strip()
        if len(value) < 3 or len(value) > 50:
            raise ValueError('Course Name is Too Short/Long')
        
        self.__course_name = value
        
    @property
    def course_book(self):
        return self.__course_book
    
    @course_book.setter
    def course_book(self, value):
        if not isinstance(value, str):
            raise TypeError('Course Book must be a String Value')
        value.strip()
        if len(value) < 3 or len(value) > 50:
            raise ValueError('Course Book is Too Short/Long')
        
        self.__course_book = value
    
    @property
    def credit_hours(self):
        return self.__credit_hours
    
    @credit_hours.setter
    def credit_hours(self, value):
        if not isinstance(value, tuple):
            raise TypeError('Credit Hours must be a Tuple')
        if len(value) != 2:
            raise ValueError('Invalid Format, Valid Format is (Theory, Lab)')
        if not all(isinstance(x, int) for x in value):
            raise ValueError('Credit Hour must be in Integer Values')
        
        self.__credit_hours = value
        
    @property
    def semester(self):
        return self.__semester
    
    @semester.setter
    def semester(self, value):
        if not isinstance(value, int):
            raise TypeError('Semester must be an Integer Value')
        if value < 1 or value > 8:
            raise ValueError('Semester must be between 1 - 8')
        
        self.__semester = value
        
    @property
    def is_optional(self):
        return self.__is_optional
    
    @is_optional.setter
    def is_optional(self, value):
        if not isinstance(value, bool):
            raise TypeError('Must be an Boolean Value')
        
    @property
    def teachers(self):
        return self.__teachers
    
    @teachers.setter
    def teachers(self, value):
        if not isinstance(value, Faculty):
            raise TypeError('Teachers must be a Faculty Object Value')
        
        return self.__teachers
    
    def update(self, **attr):
        for key, value in attr.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"""Invalid Argument '{key}'
Valid Arguments: {self.__class__.attributes}""")
        
    
        
    
class CourseList:
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Under Construction'