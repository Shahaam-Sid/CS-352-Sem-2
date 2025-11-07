from copy import copy, deepcopy

# nested list:
#appening in top-level list
original = [[1, 2],[3, 4]]
reference = original
shallow = copy(original)
deep = deepcopy(original)

original.append([5, 6])

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output
# original: [[1, 2], [3, 4], [5, 6]]
# reference: [[1, 2], [3, 4], [5, 6]]
# shallow: [[1, 2], [3, 4]]
# deep: [[1, 2], [3, 4]]


#replacing in top-level list
original = [[1, 2],[3, 4]]
reference = original
shallow = copy(original)
deep = deepcopy(original)

original[1] = 'replaced'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output:
# original: [[1, 2], 'replaced']
# reference: [[1, 2], 'replaced']
# shallow: [[1, 2], [3, 4]]
# deep: [[1, 2], [3, 4]]


#appending in nested list
original = [[1, 2],[3, 4]]
reference = original
shallow = copy(original)
deep = deepcopy(original)

original[1].append(5)

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output:
# original: [[1, 2], [3, 4, 5]]
# reference: [[1, 2], [3, 4, 5]]
# shallow: [[1, 2], [3, 4, 5]]
# deep: [[1, 2], [3, 4]]


#replacing in nested list
original = [[1, 2],[3, 4]]
reference = original
shallow = copy(original)
deep = deepcopy(original)

original[1][1] = 'replaced'

print('original:', original)
print('reference:', reference)
print('shallow:', shallow)
print('deep:', deep)
print()

#output:
# original: [[1, 2], [3, 'replaced']]
# reference: [[1, 2], [3, 'replaced']]
# shallow: [[1, 2], [3, 'replaced']]
# deep: [[1, 2], [3, 4]]