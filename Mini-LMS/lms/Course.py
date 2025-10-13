class Course:
    
    attributes = "course_id, course_name, course_book, credit_hours, semester, is_optional"
    
    def __init__(self, course_id, course_name, course_book, credit_hours, semester, is_optional):
        self.course_id = course_id
        self.course_name = course_name
        self.course_book = course_book
        self.credit_hours = credit_hours
        self.semester = semester
        self.is_optional = is_optional
        
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
Semester: {self.semester}   Optional: {self.is_optional}"""    
    
class CourseList:
    def __init__(self, array = None):
        
        if array is None:
            self._list = [None] * 5
        elif isinstance(array, list):
            if any(not isinstance(x, Course) for x in array):
                raise TypeError("Array must contain Course objects only")
            self._list = array[:]
        else:
            raise TypeError("Array must be a list or None")
    
    def display(self):
        print('-' * 50)
        print("Number of Courses: ", self.occupied_slots())
        print("Total Capacity:", len(self))
        for crs in self._list:
            if crs is not None:
                print("-=" * 25)
                print(crs)
                print("-=" * 25)
        print("-" * 20 + "END OF LIST" + "-" * 20)
        
    def add(self, crs):

        if not isinstance(crs, Course):
            raise TypeError("CourseList Only Works with Course Objects")
        
        self._check_dupe(crs.course_id)
        
        if len(self._list) == self.occupied_slots():
            self._extend_array()
            
        for i in range(len(self._list)):
            if self._list[i] is None:
                self._list[i] = crs
                return
        
    def clear_all(self):
        
        self._list = [None] * 5
        
    def index(self, by):
        
        if not isinstance(by, list):
            raise TypeError('by must be a List')
        if len(by) != 2:
            raise ValueError("by must be in this format, [name or course_id, 'course name or course id']")
        
        ind = None
        
        if by[0] == 'course_name':
            
            if not isinstance(by[1], str):
                raise TypeError('Course Name must be a String Value')
            by[1].strip()
            if len(by[1]) < 3 or len(by[1]) > 50:
                raise ValueError('Course Name is Too Short/Long')
            
            for i in range(len(self._list)):
                if self._list[i] is not None:
                    if self._list[i].course_name == by[1]:
                        ind = i
            
            if ind == None:
                raise ValueError("Name Not Matched | Course Not Found")

        elif by[0] == 'course_id':
            if not isinstance(by[1], str):
                raise TypeError('Course ID must be a String Value')
            by[1] = by[1].upper()
            if not by[1].isalnum():
                raise ValueError('Course ID must only consist of Alphabets and Numbers')
            if len(by[1]) != 5:
                raise ValueError('Course ID must consist of 5 Characters')
            
            for i in range(len(self._list)):
                if self._list is not None:
                    if self._list[i].course_id == by[1]:
                        ind = i
            if ind == None:
                raise ValueError("Course ID Not Matched | Course Not Found")
            
        else:
            raise AttributeError('Can Only Update by Course Name(course_name) or Course ID(course_id)')
        
        return ind
    
    def pop(self, index):
        
        if not isinstance(index, int):
            raise ValueError("Index must be a Integer Value")
        
        crs = self._list[index]
        
        del self[index]
        
        return crs
    
    def remove(self, id):

        index = self.index(['course_id', id])
        
        del self[index]
        
    def update_element(self, by, **attr):
        
        ind = self.index(by)
            
        self[ind].update(**attr)
        
    def _check_dupe(self, id):
        for crs in self._list:
            if crs is not None:
                if id == crs.course_id:
                    raise ValueError('This Course ID already exists in the Array')
    
    def _extend_array(self):
        temp = [None] * (len(self._list) * 2)
        
        for i in range(len(self._list)):
            temp[i] = self._list[i]
            
        self._list = temp
    
    def occupied_slots(self):
        occ_slot = 0
        for i in self._list:
            if i is not None:
                occ_slot += 1
            
        return(occ_slot)
        
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
    
    def __iter__(self):
        self.__iter_index = 0
        return self
    
    def __next__(self):
        while self.__iter_index < len(self._list):
            element = self._list[self.__iter_index]
            self.__iter_index += 1
            
            if element is not None:
                return element
            
        raise StopIteration
    
    def __str__(self):
        return "[" + ", ".join(str(crs) for crs in self._list if crs is not None) + "]"