

# set is unordered and no index, it is immutable, e.g > union & intersection <<< >>>
# union will merge objects A and B, and rep duplicate once <<< >>>
# intersection will print only A and B dup objects <<< >>>
# difference will print only what is unique to A or B and discard dup completely << >>
# symmetric difference will merge objects and discard duplicate << >>


set_num = {1, 2, 3, 4, 2, 5,1}
set_names = {'joy ', 'peter', 'obi', 'joy',}
set_mix1 = {6, 7, 2, 8, 'ely', 'billz'}
set_mix2 = {12, 13, 14, 'michael', 'kings', ('a', 'b', 'c') }


set_cities = set(('asaba', 'uyo', 'lagos', 'asaba', 'lagos'))


print('set_num : ', set_num)
print('set_num_type :', type(set_num))

print('set_names : ', set_names)
print('set_names_type :', type(set_names))

print('set_mix1 : ', set_mix1)
print('set_mix1_type :', type(set_mix1))

print('set_mix2 : ', set_mix2)
print('set_mix2_type :', type(set_mix2))

print('set_cities :', set_cities)
print('set_cities type :', type(set_cities) )

print('^ end > set and type ^'.center(50, ('-')))
print('\n')

# add will only add one object while update adds multi-objects << >>

set_num.add (6)
set_num.update ([7, 8])
print('set_num :', set_num)

print('^ end > add, update ^ '.center(50, ('-')))
print('\n')

# remove will give error but discard won't, << >>

print(set_cities)
set_cities.discard('uyo')
print(set_cities)
set_cities.remove('lagos')
print(set_cities)
set_cities.pop()
print(set_cities)

print('^ end > remove,discard,pop ^'.center(50, ('-')))
print('\n')

# union set  option 1 & 2 << >>
# result is dsame A-B or B-A << >>

set_test1 = {1, 2, 3, 4, 5, 'c'}
set_test2 = {4, 2, 'a', 'b', 'c'}
print('Data union opt 1 :', set_test1.union(set_test2) )

set_test3 = {'ely billz', 'nwoye emeka', 'eleazar nwoye'}
set_test4 = {'emeka', 'nwoye emeka'}
print('Data union opt 2 :', set_test3 | set_test4 )

print('^ end > set union ^'.center(50,('.')))
print('\n')

# intersection set  option 1 & 2 << >>
# result is dsame A-B or B-A << >>

set_test5 = {1, 2, 3, 4, 5, 'c'}
set_test6 = {4, 2, 'a', 'b', 'c'}
print('Data intersection opt 1 :', set_test5.intersection(set_test6) )

set_test7 = {'ely billz', 'nwoye emeka', 'eleazar nwoye'}
set_test8 = {'emeka', 'nwoye emeka'}
print('Data intersection opt 2 :', set_test7 & set_test8 )

print('^ end > set intersection ^'.center(50,('.')))
print('\n')

# difference set  option 1 & 2 << >>
# result  A-B diff from  B-A << >>

set_test9 = {1, 2, 3, 4, 5, 'c'}
set_test10 = {4, 2, 'a', 'b', 'c'}
print('Data diff opt 1a :', set_test9.difference(set_test10) )
print('Data diff opt 1b :', set_test10.difference(set_test9) )

set_test11 = {'ely billz', 'nwoye emeka', 'eleazar nwoye'}
set_test12 = {'emeka', 'nwoye emeka'}
print('Data diff opt 2a :', set_test11 - set_test12 )
print('Data diff opt 2b :', set_test12 - set_test11 )

print('^ end > set difference ^ '.center(50,('.')))
print('\n')

# symmetric difference set  option 1 & 2 << >>
# result  A-B diff from  B-A << >>

set_test13 = {1, 2, 3, 4, 5, 'c'}
set_test14 = {4, 2, 'a', 'b', 'c'}
print('Data symm diff opt 1a :', set_test13.symmetric_difference(set_test14) )
print('Data symm diff opt 1b :', set_test14.symmetric_difference(set_test13) )

set_test15 = {'ely billz', 'nwoye emeka', 'eleazar nwoye'}
set_test16 = {'emeka', 'nwoye emeka'}
print('Data symm dif opt 2a :', set_test15 ^ set_test16 )
print('Data symm diff opt 2b :', set_test16 ^ set_test15 )

print('^ end > set symm diff ^ '.center(50,('.')))

# membership in set << >>

print('emeka' in set_test16)
print('e' in set_test13)
print('emeka' not in set_test12)

print("end".center(50, "-"))

for name in set_names:
    print('>>', name)

print("end".center(50, "-"))

# declared value << >>
set_1 = {101,20,3,41,5,60, 12}
set_2 = {'a', 'b','a','f'}
set_3 = {1,2,3,4}
set_4 = {'b', 'c', 'a'}

# for max or min, len, any or all boolean, sorted or sum << >>
print('length of set_1 >>', len(set_1))
print('any of set_2 >>', any(set_2))
print('all of set_4 >>', all(set_2))
print('max value of set_3 >>', max(set_3))
print('min value of set_3 >>', min(set_3))
print('max value of set_1 >>', max(set_1))
print('min value of set_1 >>', min(set_1))
print('sorted set_1 >>', sorted(set_1))
print('rev-sorted set_3 >>', sorted(set_3, reverse=True))
print('sorted set_4 >>', sorted(set_4))
print('sum set_1 >>', sum(set_1))

set_5 = set_1, set_2
print('set_5 :', set_5)

# can't add nor remove
set_6 = frozenset([1,2,3,])



