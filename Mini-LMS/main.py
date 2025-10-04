from lms.Person import Student, Teacher, Batch, Faculty
from lms.Course import Course, CourseList

def run():
    try:
        
        y1_s1 = CourseList()
        
        tch1 = Teacher('Badr Sami', 65, '03000000000', 'badrsami@yahoo.com', 'AP001', 'Associate Professor', y1_s1)
        tch2 = Teacher('Nadeem Mehmoud', 59, '03000000001', 'NadeemM@hotmail.com', 'AP002', 'Associate Professor', y1_s1)
        
        teacher_list=Faculty([tch1, tch2])
        
        crs1 = Course('CS356', 'OOP', 'DSA with Python', (3, 2), 2, False, teacher_list)
        crs2 = Course("CS210", "Database Systems", "Database System Concepts by Silberschatz", (3, 1), 3, False, teacher_list)
        crs3 = Course("CS105", "Intro to Programming", "Python Crash Course", (3, 1), 1, False, teacher_list)
        crs4 = Course("CS420", "Machine Learning", "Hands-On Machine Learning with Scikit-Learn", (3, 0), 7, True, teacher_list)
        crs5 = Course("CS499", "Final Year Project", "N/A", (0, 6), 8, False, teacher_list)
        
        y1_s2 = CourseList([crs1, crs2])
        
        tch3 = Teacher('Humera Tariq', 46, '03110000000', 'humeraaa@gmail.com', 'TH009', 'Lecturer', y1_s2)
        tch4 = Teacher('Bari Ahmed Khan', 38, '03990000000', 'bak@mail.com', 'TA030', 'Teaching Associate', y1_s2)
        
        print(tch3)
        
        
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