from Person import Student, Teacher
from Course import CourseList

def run():
    try:
        courses = CourseList()
        a = Student('Muhammad Shahaam Siddiqui', 20, '03180000000', 'muhammadgc821@gmail.com',
                    'B2611000000', 2, 'CS', courses)
        
        c = Teacher('Nadeem Mehmood', 55, '03120000000', 'nadeem@hotmail.com', 'AP007', 'Associate Professor', courses)
        
        a.update(name='Badr Sami')
        
        print(a)
        
    except TypeError as e:
        print('Type Error:', e)
    except ValueError as e:
        print('Value Error:', e)
    except AttributeError as e:
        print('Attribute Error:', e)
    except Exception as e:
        print('Error:', e)
        
if __name__ == '__main__':
    run()