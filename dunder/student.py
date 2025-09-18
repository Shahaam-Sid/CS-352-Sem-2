class Student:
    count = 0
    
    def __init__(self, name, gpa, sem, rollNo):
        self.name = name
        self.gpa = gpa
        self.sem = sem
        self.rollNo = rollNo
        Student.count += 1
    
    def getInfo(self):
        print(f"""Name: {self.name}
GPA: {self.gpa}
Semester: {self.sem}
Roll No.: {self.rollNo}""")
        
    def __repr__(self):
        return f"Student ('{self.name}', {self.gpa}, {self.sem}, '{self.rollNo}')"
    
    def studentStatus(self, ideal):
        if self.gpa > ideal.gpa:
            print("Great Work, Keep it up")
        elif self.gpa < 2.5:
            print("Not Satisfactory")
        else:
            print("Do More")
            
    def __eq__(self, other):
        if self.gpa == other.gpa:
            return f"GPA of {self.name} is equals to {other.name}"
        elif self.gpa > other.gpa:
            return f"GPA of {self.name} is greater then {other.name}"
        else:
            return f"GPA of {self.name} is lesser then {other.name}"
            
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "gpa":
            return self.gpa
        elif key == "semester":
            return self.sem
        elif key == "roll":
            return self.rollNo
        else:
            return f"Wrong Key Entered"
        
    @classmethod
    def getCount(cls):
        return f"Total Entries: {cls.count - 1}"
        
        
idealStudent = Student("Ideal", 3.7, 8, "B00000")
s1 = Student("Kamran Ahmed", 3.8, 5, "B30917")
s2 = Student("Taimoor", 3.6, 2, "B40677")

print(Student.getCount())

print()

s1.getInfo()

print()

print(s1)

print()

s1.studentStatus(idealStudent)

print()

print(s1 == s2)

print()

print(s1["semester"])