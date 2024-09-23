

# dict with integer keys << >>

print('dictionary with integer keys'.center(50, ('-')))
print('\n')

dict_int = {1: 'mango', 2: 'apple', 3: 'dog' }
print("dict_int :", dict_int)
print("dict_int type :", type(dict_int))

# dict with strings keys << >>
print('dictionary with strings keys'.center(50, ('-')))
print('\n')

dict_str = {'Fruit': 'Mango', 'Animal': 'dog', 'name': 'ely' }
print("dict_str :", dict_str)
print("dict_str type :", type(dict_str))

# dict with mixed keys << >>
print('dictionary with mixed keys'.center(50, ('-')))
print('\n')

dict_mix = {'Dept': 'Drills', 'Progrm': ['7214/2245-2295'], 73: 'Total'  }
print("dict_mix :", dict_mix)
print("dict_mix type :", type(dict_mix))

# dict with function ()  for list > [[ ]] and tuple > (( ))   << >>
print('dictionary with () '.center(50, ('-')))
print('\n')

dict_funt = dict({'Dpt': 'Client', 'Sub dpt': 'Qc', 'name': "Emeka" })
print("dict_funt :", dict_funt)
print("dict_funt type :", type(dict_funt))

print('End '.center(50, ('-')))
print('\n')

# dict membership type 1 << >>

print('Dict membership '.center(50, ('-')))

emplo_id = { 'ID-2001': 'Nwoye Emeka',
             'ID-2002': 'Jack Unknown',
             'ID-2003': 'Timothy Ekong',
             'ID-2004': 'Pius Beke',
           }
emp_id = 'ID-2002'
if emp_id in emplo_id:
    name = emplo_id [emp_id]
    print('Employee ID is: {}, Employee name is: {}'.format(emp_id, name))
else:
    print('Employee ID {}, not found'.format(emp_id) )

print('\n')


print('Membership using if, elif and input class :')

# membership using input my code proud me !!! << >>

id_selected = input('Enter ID No :')
emp_0 = 'ID-2001'
emp_1 = 'ID-2002'
emp_2 = 'ID-2003'
emp_3 = 'ID-2004'
if id_selected == emp_0 in emplo_id:
    name = str(emplo_id [emp_0])
    print('Employee ID is: {}, Employee Name is: {}'.format(emp_0, name))
elif id_selected == emp_1 in emplo_id:
    name = str(emplo_id [emp_1])
    print('Employee ID is: {}, Employee Name is: {}'.format(emp_1, name))
elif id_selected == emp_2 in emplo_id:
    name = emplo_id[emp_2]
    print('Employee ID is: {}, Employee Name is: {}'.format(emp_2, name))
elif id_selected == emp_3 in emplo_id:
    name = emplo_id[emp_3]
    print('Employee ID is: {}, Employee Name is: {}'.format(emp_3, name))
else:
    print('Employee ID not found' )

print('End '.center(50, ('-')))
print('\n')

emplo_info = { 'Name': 'Nwoye Emeka',
             'Depart': 'Client QC',
             'Date of employment': '01/12/2022',
             'Salary': '#130,000.00'
           }
name = emplo_info.get('Name')
dpt = emplo_info.get('Depart')
date = emplo_info.get('Date of employment')
salary = emplo_info.get('Salary')

print('{} Works in Dpt of: {}. Job engagement Date: {}. Salary or rate: {}'.format(name, dpt, date, salary ))

print('-----')


emplo_info['Depart'] = 'Client QC'
emplo_info['Salary'] = '#200,000.00'

Depart = emplo_info.get('Depart')
Salary = emplo_info.get('Salary')
print('{} Works in Dpt of: {}. Job engagement Date: {}. Salary or rate: {}'.format(name, Depart, date, Salary ))

emplo_info["Camp"] = "Jagioo Energy"
emplo_info["Position"] = "Super Qc"
emplo_info["Rank"] = "2"

print(emplo_info.get)


# to del list & empty list <<< >>>
# del emplo_ifo
# emplo_ifo = []  <#or> emplo_ifo.clear()
# emplo_ifo.pop()

print('\n')
print('DICTIONARY PART 2 '.center(50, ('>')))
print('\n')

# dictionary using keys << >>

print('Dict using dict.keys '.center(50, ('-')))


emplo_id = { 'ID-2001': 'Nwoye Emeka',
             'ID-2002': 'Jack Unknown',
             'ID-2003': 'Timothy Ekong',
             'ID-2004': 'Pius Beke',
           }

dict_key = emplo_id.keys()
print(dict_key)
print(type(dict_key))

print('\n')
print('<< unpack  itmes >>')
for dict_id in emplo_id:
    print(dict_id + ' : ' + emplo_id[dict_id] )

# Dictionary using values << >>

print('Dict using dict.values '.center(50, ('-')))

print('\n')

dict_value = emplo_id.values()
print(dict_value)
print('dict_value type :',type(dict_value))

print('\n')
print('<< unpack  itmes >>')

for name in emplo_id.values():
    print(name)

# Dictionary using items << >>

print('Dict using dict.items '.center(50, ('-')))
print('\n')

dict_item = emplo_id.items()
print(dict_item)

print('dict_value type :',type(dict_item))
print('\n')

print('<< unpack  itmes >>')

for dict_item, name in emplo_id.items():
    print(dict_item + ' : ' + name)


# dictionary with long objects << >>

print('\n')
print('when you have long list of objects use list function () and sort afterward'.center(70, ('-')))
print('\n')

qc_list = {'name': ['nwoye', 'emeka', 'joy', 'peace'],
           'No': [1,2,15,3,4, 13,5,6,7,8,9,10],
           'star': [2,3,1,1,2,1,1,3,1,1,],


          }

dict_list = list(qc_list.keys())
print('dict_using_list ', dict_list)
dict_list.sort()
print('dict_list.sort', dict_list)
print('\n')

# dictionary using fromkeys used to get keys printed << >>

dict_fromkey = {1,3,5,6,2,7,8,9,0}

qc_fromkey = dict.fromkeys(dict_fromkey, 'Default')
print('Default_opt 1 :', qc_fromkey)
print('\n')

dict_fromkey2 = {1,2,3,4,5,6,7,8,9}

default_value = 'Default_value'
qc_fromkey2 = dict.fromkeys(dict_fromkey2, default_value)
print('Default_opt 1 :', qc_fromkey2)
print('\n')

# dictionary pop, update then use list() and fromkeys() to sort objects << >>

dict_fromkey3 = {'A': '1', 'B': '3', 'C': '5', 'D': '7', 'E':'9'}
print('dict_key3 >>', dict_fromkey3)

dict_fromkey3.popitem()
print('dict_fromkey3 pop :',dict_fromkey3)


dict_fromkey3.update({'F': '11', 'G': '13', 'E': '9' })
print('Updated :', dict_fromkey3)
print('Type', type(dict_fromkey3))

# list and fromkeys() to sort << >>
dict12 = list(dict_fromkey3.items())
dict12.sort()
print('Sorted :', dict12)
print('Type', type(dict12))

