from ast import List


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
        if not value.isdecimal:
            raise ValueError('Serial Number must obly contain Integers')
        if not len(value) == 7:
            raise ValueError('Serial Number must contain 7 digits')
        
        self._s_no = value
    
    def __str__(self):
        return f"Name: {self.name}, Field: {self.field}, Semester: {self.sem}, Serial No.: {self.s_no}"
    
    
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
    
s1 = Students('Muhammad Shahaam Siddiqui', 'CS', 2, '0000001')
s2 = Students('Muhammad Hanzala Siddiqui', 'DS', 1, "0000002")
s3 = Students('Muhammad Umer Farooq', 'AI', 4, '0000003')

l = ListStudents([s1, s2, s3])

reversed(l)

print(l)