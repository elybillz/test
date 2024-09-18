

print('dictionary with integer keys'.center(50, ('-')))
print('\n')

dict_int = {1: 'mango', 2: 'apple', 3: 'dog' }
print("dict_int :", dict_int)
print("dict_int type :", type(dict_int))

print('dictionary with strings keys'.center(50, ('-')))
print('\n')

dict_str = {'Fruit': 'Mango', 'Animal': 'dog', 'name': 'ely' }
print("dict_str :", dict_str)
print("dict_str type :", type(dict_str))

print('dictionary with mixed keys'.center(50, ('-')))
print('\n')

dict_mix = {'Dept': 'Drills', 'Progrm': ['7214/2245-2295'], 73: 'Total'  }
print("dict_mix :", dict_mix)
print("dict_mix type :", type(dict_mix))

print('dictionary ()'.center(50, ('-')))
print('\n')

dict_funt = dict({'Dpt': 'Client', 'Sub dpt': 'Qc', 'name': "Emeka" })
print("dict_funt :", dict_funt)
print("dict_funt type :", type(dict_funt))

print('End '.center(50, ('-')))
print('\n')

emplo_id = { 'ID-2001': 'Nwoye Emeka',
             'ID-2002': 'Jack Unknown',
             'ID-2003': 'Timothy Ekong'
           }
emp_id = 'ID-2002'
if emp_id in emplo_id:
    name = emplo_id [emp_id]
    print('Employee ID is {}, Employee name is {}'.format(emp_id, name))
else:
    print('Employee ID {}, not found'.format(emp_id) )

print('\n')

emp_0 = 'ID-2001'
emp_1 = 'ID-2002'
emp_2 = 'ID-2003'

id_selected = input('Enter ID No :')
if id_selected in emplo_id == emp_0:
    name = emplo_id [emp_0]
    print('Employee ID is {}, Employee name is {}'.format(emp_0, name))
elif id_selected in emplo_id == emp_1:
    name1 = emplo_id[emp_1]
    print('Employee ID is {}, Employee name is {}'.format(emp_1, name1))
elif id_selected in emplo_id == emp_2:
    name2 = emplo_id[emp_2]
    print('Employee ID is {}, Employee name is {}'.format(emp_2, name2))
else:
    print('Employee ID not found' )




