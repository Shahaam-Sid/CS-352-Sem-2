from lms.Person import Student, Teacher, Batch, Faculty
from lms.Course import Course, CourseList

def run():
    try:
        
        # Story:
        
        # 1. Create Empty Student List
        dcs = Batch()
   
        # 2. Add Student(Ahmed, Aisha, Bilal)
        course_secondsem = CourseList([Course('CS352', 'Object Oriented Concepts & Programming', 'Data Structure & Algorithm in Python',
                                              (3, 1), 2, False),
                                       Course('CS354', 'Digital Logic Design', 'Digital Fundamentals',
                                              (2, 1), 2, False),
                                       Course('CS356', 'Linear Algebra', 'Elementary Linear ALgebra',
                                              (3, 0), 2, False),
                                       Course('CS358', 'Descrete Structure', 'Not Specified',
                                              (3, 0), 2, False),
                                       Course('CS360', 'Communication and Presentation Skills', 'Not Specified',
                                              (3, 0), 2, False),
                                       Course('CS362', 'Ideology and Constitution of Pakistan', 'Not Specified',
                                          (2, 0), 2, False)])

        std1 = Student('Ahmed Khan', 20, '03234567890', 'ahmedk@yahoo.com', 'B2411000091', 2, 'CS', course_secondsem)
        std2 = Student('Ayesha binte Abi Bakr', 19, '03180987654', 'ayesha06@gmail.com', 'B2411000035', 2, 'CS', course_secondsem)
        std3 = Student('Bilal Siddiqui', 22, '03181191750', 'bilalsid@gmail.com', 'B2411000005', 2, 'CS', course_secondsem)
        
        dcs.admit(std1)
        dcs.admit(std2)
        dcs.admit(std3)
        
        # 3. New Student joins mid semester
        std_new = Student('Muhammad Umer Farooq', 19, '03265789393', 'umer@gmail.com', 'B2411000185', 2, 'CS', course_secondsem)
        dcs.put(1, std_new)
        
        
        # 4a. Search Student by Seat No.
        index_of_std = dcs.index(['seat_no', 'B2411000035'])
        print(dcs[index_of_std], '\n')
        
        # 4b. Search Student by Name
        index_of_std = dcs.index(['name', 'Muhammad Umer Farooq'])
        print(dcs[index_of_std], '\n')
        
        # 5. Student Changes its Phone Number and Age
        dcs.update_element(['name', 'Muhammad Umer Farooq'], age = 18, contact = '03265789939')
        print(dcs[1], '\n')
        
        # 6. Student Leaves the Departement
        dcs.remove('B2411000005')
    
        #7. Checks the status of The Department
        dcs.display()
                
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