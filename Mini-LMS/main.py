from lms.Person import Student, Teacher, Batch, Faculty
from lms.Course import Course, CourseList

def run():
    try:
        
        crs1 = Course("CS356", "OOP", "DSA with Python", (3, 2), 2, False)
        crs2 = Course("CS210", "Database Systems", "Database System Concepts by Silberschatz", (3, 1), 3, False)
        crs3 = Course("CS105", "Intro to Programming", "Python Crash Course", (3, 1), 1, False)
        crs4 = Course("CS420", "Machine Learning", "Hands-On Machine Learning with Scikit-Learn", (3, 0), 7, True)
        crs5 = Course("CS499", "Final Year Project", "N/A", (0, 6), 8, False)
        
        crslist = CourseList()
        
        crslist.add(crs1)
        crslist.add(crs2)
        crslist.add(crs3)
        
        crslist.update_element(['name', 'OOP'], credit_hours=(4, 0))
        
        crslist.display()
        
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