from copy import deepcopy, copy


# Lists:
#Appending

original = ['John', 'Jhonny', 'Jack']
reference = original
shallow = copy(original)
deep = deepcopy(original)

original.append('Jam')

#replacing
print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output:
# original: ['John', 'Jhonny', 'Jack', 'Jam']
# reference: ['John', 'Jhonny', 'Jack', 'Jam']
# shallow: ['John', 'Jhonny', 'Jack']
# deep: ['John', 'Jhonny', 'Jack']


original = ['John', 'Jhonny', 'Jack']
reference = original
shallow = copy(original)
deep = deepcopy(original)

original[1] = 'Julie'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)


#output
# original: ['John', 'Julie', 'Jack']
# reference: ['John', 'Julie', 'Jack']
# shallow: ['John', 'Jhonny', 'Jack']
# deep: ['John', 'Jhonny', 'Jack']