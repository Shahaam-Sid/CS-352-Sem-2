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
        
        self.__is_optional = value
        
    @property
    def teachers(self):
        return self.__teachers
    
    @teachers.setter
    def teachers(self, value):
        from .Person import Faculty
        if not isinstance(value, Faculty):
            raise TypeError('Teachers must be a Faculty Object Value')
        
        self.__teachers = value
    
    def update(self, **attr):
        for key, value in attr.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"""Invalid Argument '{key}'
Valid Arguments: {self.__class__.attributes}""")
                
    def __str__(self):
        return f"""Course Name: {self.course_name}  Course ID: {self.course_id}
Credit Hours: {self.credit_hours}     Course Book: {self.course_book}
Semester: {self.semester}   Optional: {self.is_optional}
Teachers: {', '.join(x.name for x in self.teachers)}
"""

        
    
        
    
class CourseList:
    def __init__(self, array = None):
        
        if array is None:
            self._list = []
        elif isinstance(array, list):
            if any(not isinstance(x, Course) for x in array):
                raise TypeError("Array must contain Course objects only")
            self._list = array[:]
        else:
            raise TypeError("Array must be a list or None")
    
    def display(self):
        
        print("No. of Courses:", len(self))
        for crs in self._list:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(crs)
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("++++++END OF LIST++++++")
        
    def add(self, crs):

        if not isinstance(crs, Course):
            raise TypeError("CourseList Only Works with Course Objects")
        
        initial_lenght = len(self._list)
        final_lenght = initial_lenght + 1
        
        new_list = [None] * final_lenght
        
        for i in range(initial_lenght):
            new_list[i] = self._list[i]
            
        new_list[-1] = crs
        
        self._list = new_list
        
    def clear_all(self):
        
        self._list = []
        
    def index(self, c_id):

        if not isinstance(c_id, str):
            raise TypeError('Course ID must be a String Value')
        c_id = c_id.upper()
        if not c_id.isalnum():
            raise ValueError('Course ID must only consist of Alphabets and Numbers')
        if len(c_id) != 5:
            raise ValueError('Course ID must consist of 5 Characters')
        
        for i in range(len(self._list)):
            if self._list[i].course_id == c_id:
                return i
            
        raise ValueError("Course ID Not Matched | Course Not Found")
    
    def pop(self, index):
        
        if not isinstance(index, int):
            raise ValueError("Index must be a Integer Value")
        
        crs = self._list[index]
        
        del self[index]
        
        return crs
    
    def remove(self, id):

        index = self.index(id)
        
        del self[index]
        
    def __contains__(self, crs):
        if not isinstance(crs, Course):
            raise TypeError("CourseList Only Works with Course Objects")
        
        for value in self._list:
            if crs == value:
                return True
            
        return False
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        
        if index < 0:
            if len(self._list) >= -(index):
                return self._list[index]
            else:
                raise IndexError(f"Index Not Found CourseList Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                return self._list[index]
            
            else:
                raise IndexError(f"Index Not Found CourseList Contains {len(self._list)} items") 
        
    
    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not isinstance(value, Course):
            raise TypeError("Value must be Course Object")
        
        if index < 0:
            if len(self._list) >= -(index):
                self._list[index] = value
            else:
                raise IndexError(f"Index Not Found CourseList Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                self._list[index] = value
            
            else:
                raise IndexError(f"Index Not Found CourseList Contains {len(self._list)} items")
    
    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
            
        if index < 0:
            index = len(self._list) + index
    
        if index < 0 or index >= len(self._list):
            raise IndexError(f"Index Not Found CourseList Contains {len(self._list)} items")
            
        new_list = [None] * (len(self._list) - 1)
        j = 0
        for i in range(len(self._list)):
            if i == index:
                continue
            new_list[j] = self._list[i]
            j += 1
                
        self._list = new_list
    
    def __len__(self):
        lenght = 0
        for _ in self._list:
            lenght += 1
                
        return lenght
    
    def __str__(self):
        return "[" + ", ".join(str(crs) for crs in self._list) + "]"