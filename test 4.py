

# for list_nested <<< >>>
list_nested = [1,2,3,4], ['a', 'b', 'c', 'd'], ['joy', 'peter']
print(list_nested)
print(list_nested[0][3])

#for append <<< >>>
list_nested1 = [1,2,3,4]
print(list_nested1)

list_nested1.append (5)
print(list_nested1)

list_nested1.extend(['c', 'f', 'g'] )
print(list_nested1)

list_nested1[5] = "e"
print(list_nested1)

list_nested1[0:5] = ['a', 'b', 'c', 'd']
print(list_nested1)

list_nested1.insert(8, 'h')
print(list_nested1)

# for del class <<< >>
del list_nested1 [7]
print(list_nested1)

list_nested1.remove('g')
print(list_nested1)
list_nested1.pop()
print(list_nested1)

list_nested1.pop()
print(list_nested1)


# to del list & empty list <<< >>>
# list_nested1 = []
# del list_nested1
