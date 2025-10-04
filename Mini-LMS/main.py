from lms.Person import Student, Teacher, Batch, Faculty
from lms.Course import Course, CourseList

def run():
    try:
        y1_s1 = CourseList()
        tch1 = Teacher('Badr Sami', 65, '03000000000', 'badrsami@yahoo.com', 'AP001', 'Associate Professor', y1_s1)
        tch2 = Teacher('Nadeem Mehmoud', 59, '03000000001', 'NadeemM@hotmail.com', 'AP002', 'Associate Professor', y1_s1)
        tch3 = Teacher('Humera Tariq', 46, '03110000000', 'humeraaa@gmail.com', 'TH009', 'Lecturer', y1_s1)
        tch4 = Teacher('Bari Ahmed Khan', 38, '03990000000', 'bak@mail.com', 'TA030', 'Teaching Associate', y1_s1)
        
        fc = Faculty([tch1, tch2, tch3])
        fc.place(1, tch4)
        fc.remove('TA030')
        print(len(fc))
        
        
        
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