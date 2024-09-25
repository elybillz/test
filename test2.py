

#from test_function import cal_sum
#from Scripts.testme import var_sum
# import math as m or import pi as p \end\ math. or m., pi. or p.
#import importlib
# importlib.reload(test_function)

# print(__name__ + 'initialization')  mypkg/__init__.py/
# init folder should __all__ = [ input name of your modules with quotation and coma   ]

# to import all package use >> from mypkg.subpkg import *

# import mypkg.subkg.mod22 as mod22


"""
docstring
"""
from dask.multiprocessing import exceptions

# print('to prnt docstring', qc_date.__doc__)


# write to file << >>

myfile = 'Qc_log.txt'

file_agent = open(myfile, 'w')

file_agent.write('1: write something ')

file_agent.close()

# PART2

myfile = 'Qc_log_2.txt'

with open(myfile, 'w') as file_agent:

    file_agent.write('1: write something \n')

    file_agent.close()

# Append to file << >>

myfile = 'Qc_log_2.txt'

with open(myfile, 'a') as file_agent:

    file_agent.write('2: Lets append something \n ')

print('END..file..open..write..>>>>>>')

from datetime import date

try:

    year_of_birth = input('Enter your year date of birth :')

    current_year = int(date.today().year)

    print(current_year - int(year_of_birth))
except ValueError as ve:
    print('invalid year !!')
    print(type(ve))
    print(ve)

print('END...string..exception...>>>>>>')

list_try = ['a', 'b', 'c', 'd', 'e', 'g']

try:
    indent_value = int(input('Enter index num :'))
    print(list_try[indent_value])
except IndexError as ie:
    print('Wrong index value !!')
    print(type(ie))
    print(ie)

except ValueError as ve:
    print('Error: you have entered a wrong value !!')
    print(type(ve))
    print(ve)

except exceptions as e:
    print(e)

print('END...list..exception...>>>>>>')

