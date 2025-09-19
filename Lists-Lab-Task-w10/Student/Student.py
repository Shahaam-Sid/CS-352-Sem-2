class Students:
    """
    A Class that Creates Student Objects
    """
    
    def __init__(self, name, field, sem, s_no):
        """
        Args:
            name (str)
            field (str): Can only be 'CS', 'DS, 'SE', 'AI'
            sem (int): Can only be 1 to 8
            s_no (str): Must contain 7 digits
        """
        
        self.name = name
        self.field = field
        self.sem = sem
        self.s_no = s_no
        
    @property
    def name(self):
        return self._name 
    
    @property
    def field(self):
        return self._field
    
    @property
    def sem(self):
        return self._sem
    
    @property
    def s_no(self):
        return self._s_no
    
    @name.setter
    def name(self, value):
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError('Name must be a String')
        if len(value) == 0:
            raise ValueError('Name cannot be empty')
        if any(not x.isalpha() for x in value.split()):
            raise ValueError("Name can only contain Alphabets")

        self._name = value
        
    @field.setter
    def field(self, value):
        if not isinstance(value, str):
            raise TypeError('Field must be a String')
        if value not in ['CS', 'SE', 'AI', 'DS']:
            raise ValueError("Invalid Field | Valid: ['CS', 'SE', 'AI', 'DS']")
        
        self._field = value
        
    @sem.setter
    def sem(self, value):
        if not isinstance(value, int):
            raise TypeError('Semester Must be a Integer Value')
        if value not in range(1, 9):
            raise ValueError("Thier exist only 8 Semesters")
        
        self._sem = value
        
    @s_no.setter
    def s_no(self, value):
        if not isinstance(value, str):
            raise TypeError('Serial Number must be a String')
        if not value.isdecimal():
            raise ValueError('Serial Number must obly contain Integers')
        if not len(value) == 7:
            raise ValueError('Serial Number must contain 7 digits')
        
        self._s_no = value
    
    def __str__(self):
        return f"Name: {self.name}, Field: {self.field}, Semester: {self.sem}, Serial No.: {self.s_no}"
    
    def __repr__(self):
        return f"Students(name='{self.name}', field='{self.field}', sem={self.sem}, s_no='{self.s_no}')"

    
    
class ListStudents:
    def __init__(self, array = None):
        
        if array is None:
            self._list = []
        elif isinstance(array, list):
            if any(not isinstance(x, Students) for x in array):
                raise TypeError("Array must contain Student objects only")
            self._list = array[:]
        else:
            raise TypeError("Array must be a list or None")
        
    def display(self):
        """
        Displays Students
        """
        
        print("No. of Students:", len(self))
        for card in self._list:
            print(card)
            
    def admit(self, student):
        """
        Creates a new index and adds Student
        Args:
            student (Student)

        """

        if not isinstance(student, Students):
            raise TypeError("ListStudents Only Works with Students Objects")
        
        initial_lenght = len(self._list)
        final_lenght = initial_lenght + 1
        
        new_list = [None] * final_lenght
        
        for i in range(initial_lenght):
            new_list[i] = self._list[i]
            
        new_list[-1] = student
        
        self._list = new_list
        
    def clear_all(self):
        """
        Empties the List
        """
        self._list = []
   
    def index(self, id):
        """
        Returns the Index of The Given Serial No.

        Args:
            id (str)

        Returns:
            int
        """
        if not isinstance(id, str):
            raise TypeError('Serial Number must be a String')
        if not id.isdecimal:
            raise ValueError('Serial Number must only contain Integers')
        if not len(id) == 7:
            raise ValueError('Serial Number must contain 7 digits')
        
        for i in range(len(self._list)):
            if self._list[i].s_no == id:
                return i
            
        raise ValueError("ID Not Matched | Credit Card Not Found")
        
    def put(self, index, student):
        """
        Inserts the Student to the
        given Index

        Args:
            index (int)
            student (Student)
        """
        
        if not isinstance(index, int):
            raise TypeError("Index must be an Integer Value")
        if not isinstance(student, Students):
            raise TypeError("Can only insert Students object")
        
        n = len(self._list)
        
        if index < 0:
            index = n + index
        
        new_list = [None] * (n + 1)
        
        for i in range(n + 1):
            if i < index:
                new_list[i] = self._list[i]
            if i == index:
                new_list[i] = student
            if i > index:
                new_list[i] = self._list[i - 1]
                
        self._list = new_list
        
    def include(self, collection):
        """
        Adds the entered List of Students to the
            end of the existing list

        Args:
            collection (List)
        """
        if not isinstance(collection, list):
            raise TypeError("Collection must be a List")
        if any(not isinstance(x, Students) for x in collection):
            raise TypeError("Collection must Only contain Students Objects")
        
        for i in collection:
            self.admit(i)
            
    def pop(self, index):
        """
        Removes the Student from the given Index and returns the

        Args:
            index (int)
        
        Returns:
            Student
        """
        
        if not isinstance(index, int):
            raise ValueError("Index must be a Integer Value")
        
        student = self._list[index]
        
        del self[index]
        
        return student
    
    def remove(self, id):
        """
        Removes the Student of the given Serial No.

        Args:
            id (str)
        """

        index = self.index(id)
        
        del self[index]
            
    def get_field(self, f):
        """
        Returns a List of the Selected Field

        Args:
            f (str): can only be 'CS', 'SE', 'AI', 'DS'

        Returns:
            ListStudents
        """
        
        if not isinstance(f, str):
            raise TypeError('Field must be a String')
        if f not in ['CS', 'SE', 'AI', 'DS']:
            raise ValueError("Invalid Field | Valid: ['CS', 'SE', 'AI', 'DS']")
                
        return ListStudents([student for student in self._list if student.field == f])
    
    def sort(self):
        """
        Sorts by Field inOrder of:
            1. CS
            2. SE
            3. AI
            4. DS

        Returns:
            ListStudents
        """
        cs = self.get_field('CS')
        se = self.get_field('SE')
        ai = self.get_field('AI')
        ds = self.get_field('DS')
        
        new_list = []
        new_list.extend(cs._list)
        new_list.extend(se._list)
        new_list.extend(ai._list)
        new_list.extend(ds._list)
        
        return ListStudents(new_list)
        
    def __contains__(self, student):
        if not isinstance(student, Students):
            raise TypeError("ListStudents Only Works with Credit Card Objects")
        
        for card in self._list:
            if student == card:
                return True
            
        return False
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        
        if index < 0:
            if len(self._list) >= -(index):
                return self._list[index]
            else:
                raise IndexError(f"Index Not Found ListStudents Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                return self._list[index]
            
            else:
                raise IndexError(f"Index Not Found ListStudents Contains {len(self._list)} items")    
    
    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not isinstance(value, Students):
            raise TypeError("Value must be Student Object")
        
        if index < 0:
            if len(self._list) >= -(index):
                self._list[index] = value
            else:
                raise IndexError(f"Index Not Found ListStudents Contains {len(self._list)} items")
            
        else:
            if len(self._list) > index:
                self._list[index] = value
            
            else:
                raise IndexError(f"Index Not Found ListStudents Contains {len(self._list)} items")
    
    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
            
        if index < 0:
            index = len(self._list) + index
    
        if index < 0 or index >= len(self._list):
            raise IndexError(f"Index Not Found. ListStudents Contains {len(self._list)} items")
            
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
    
    def __reversed__(self):
        n = len(self._list)
        new_list = [None] * n
        for i in range(n):
            new_list[i] = self._list[n - 1 - i]
            
        self._list = new_list
        
    def __str__(self):
        return "[" + ", ".join(str(card) for card in self._list) + "]"