from copy import copy, deepcopy


#dict
#replacing in top level object
original = {
    'name': 'John',
    'courses': ['OOP', 'DLD']
}
reference = original
shallow = copy(original)
deep = deepcopy(original)

original['courses'] = ['OOP', 'LA']

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: {'name': 'John', 'courses': ['OOP', 'LA']}
# reference: {'name': 'John', 'courses': ['OOP', 'LA']}
# shallow: {'name': 'John', 'courses': ['OOP', 'DLD']}
# deep: {'name': 'John', 'courses': ['OOP', 'DLD']}


#replacing in low level object
original = {
    'name': 'John',
    'courses': ['OOP', 'DLD']
}
reference = original
shallow = copy(original)
deep = deepcopy(original)

original['courses'][1] = 'Replaced'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: {'name': 'John', 'courses': ['OOP', 'Replaced']}
# reference: {'name': 'John', 'courses': ['OOP', 'Replaced']}
# shallow: {'name': 'John', 'courses': ['OOP', 'Replaced']}
# deep: {'name': 'John', 'courses': ['OOP', 'DLD']}