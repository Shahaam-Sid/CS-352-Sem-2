from Person import Student
from Course import CourseList

try:
    courses = CourseList()
    a = Student('Muhammad Shahaam Siddiqui', 20, '03181189075', 'muhammadgc821@gmail.com',
                'B2411000101', 2, 'CS', courses)
    print(a)
    
except TypeError as e:
    print('Type Error:', e)
except ValueError as e:
    print('Value Error:', e)
except AttributeError as e:
    print('Attribute Error:', e)
except Exception as e:
    print('Error:', e)