from copy import copy, deepcopy


# changing integer value
class Students:
    def __init__(self, name, age, course):
        self.name = name 
        self.age = age
        self.course = course
        
    def __str__(self):
        return f"{self.name} | {self.age} | {self.course}"
    


original = Students('John', 19, ['OOP', 'DLD'])
reference = original
shallow = copy(original)
deep = deepcopy(original)

original.age = 21

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: John | 21 | ['OOP', 'DLD']
# reference: John | 21 | ['OOP', 'DLD']
# shallow: John | 19 | ['OOP', 'DLD']
# deep: John | 19 | ['OOP', 'DLD']


#changing at top level
original = Students('John', 19, ['OOP', 'DLD'])
reference = original
shallow = copy(original)
deep = deepcopy(original)

original.course = 'Replaced'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: John | 19 | Replaced
# reference: John | 19 | Replaced
# shallow: John | 19 | ['OOP', 'DLD']
# deep: John | 19 | ['OOP', 'DLD']


#changing at low level
original = Students('John', 19, ['OOP', 'DLD'])
reference = original
shallow = copy(original)
deep = deepcopy(original)

original.course[0] = 'Replaced'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: John | 19 | ['Replaced', 'DLD']
# reference: John | 19 | ['Replaced', 'DLD']
# shallow: John | 19 | ['Replaced', 'DLD']
# deep: John | 19 | ['OOP', 'DLD']