
# for list class <<< >>>
name = ["JOY", "peter", "mark"]
no = [1, 2, 3, 4,]
print(name [1:2])
print(no [:-3])
print(name.index('mark'))
print(name.index("peter") )
print(type(name))

# for list combination <<< >>>
print(name + no)
newl = no * 2
print(newl)
print('--------------------------------------------')




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

# for del class e.g remove, pop <<< >>

del list_nested1 [7]
print(list_nested1)

list_nested1.remove('g')
print(list_nested1)
list_nested1.pop()
print(list_nested1)

list_nested1.pop()
print(list_nested1)

a, b, c, d = list_nested1
print(d, c, b, a)

print("end".center(50, "-"))

# for searching object in list & for loop condition listing object in list << >>
# for membership e.g loop, tuple, set << >>

print('d' in list_nested1)
print('e' in list_nested1)
print('d' not in list_nested1)

print("end".center(50, "-"))
for name in list_nested1:
    print('>>', name)

print('end'.center(50, ('-')))

# to del list & empty list <<< >>>
# del list_nested1
# list_nested1 = []  <#or> list_nested.clear

# for count, len, reverse, sort, sort/reverse <<< >>>
#  print(len(list_nested1))
#print("count", list_nested1.count('b'))
# list_nested1.reverse()
# list_nested1.sort()
# list_nested1.sort(reverse=True)

# to copy object to new list <<< >>>
#list_nested2 = list_nested1.copy()
#print('new', list_nested2 )
# for list_nested <<< >>>




