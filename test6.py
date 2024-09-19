from IPython.core.guarded_eval import dict_keys
from mypyc.primitives.dict_ops import dict_item_iter_op

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
