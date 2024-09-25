from odbc import dataError
from param.ipython import message

# function << >>

print('Format1......................')
def print_message():
    print("PART 1".center(50, ('$')))
    print('hello dear')

# used to call function multi X
print_message()
print_message()

print('Format 2....................>>>>')

def print_message(message):
    print(message)

print_message('opt2 hello dear')

print('Format 3....................>>>>')

def print_message3(message, num,):
    print(str(num), ' : ' + message)

message1 = 'format 3A'
message2 = 'format 3B'
message3 = 'format 3C'

# example1
print_message3(message1, 50)
print_message3(message2, 10)
#example 2
print_message3(message= message3, num = 20, )

print('Format 4....................>>>>>')

def print_message4(message= 'alert', num= 204, level= 'error'):
    print(str(num), ' : ' + message, ' : ' + level)

print_message4()

# for undefined parameter << >>
print('Format 5....................>>>>>')

def print_message5(semester, level, *year):
    print(str(level), ' : ' + semester)
    print(year)

message1 = '1st semester'

print_message5(message1, 300, 2024 )

print('Format 6....................>>>>>')

def print_kwagrs(**kwargs):
    print(kwargs)
    print(type(kwargs))

print_kwagrs(Delta = 'Asaba', FCT = 'Abuja')

# part 2 << >>
print('PART 2....................>>>>>')
def print_kwagrs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    if len(kwargs):
        for items in kwargs:
            print('{} is the capital of {}'.format(kwargs[items], items) )

print_kwagrs(Delta = 'Asaba', FCT = 'Abuja')

print('\n')
print('function for adding >>>>>')

# adding using sum << >>
def sum(num1,  num2):
    print('summing>>')
    add = num1 + num2
    return add
total = sum(10, 5)
print(str(total))

# adding using add << >>
def add(num1,  num2):
    print('adding>>')
    add = num1 + num2
    return add
total = add(15, 20)
print(str(total))


print('\n')
print('non-function converting to function >>>>>')

num1 = 5
num2 =  5

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2
reminder = num1 % num2
quotient = num1 // num2

print('The sum of {} and {} : {}'.format(num1, num2, sum))
print('The diff of {} and {} : {}'.format(num1, num2, diff))
print('The prod of {} and {} : {}'.format(num1, num2, prod))
print('The div of {} and {} : {}'.format(num1, num2, div))
print('The reminder of {} and {} : {}'.format(num1, num2, reminder))
print('The quotient of {} and {} : {}'.format(num1, num2, quotient))

# part 2 << >>
print('\n')
print('PART 2-FORMAT2......convert.......to.....function.......>>>>>')

def cal_sum(num3, num4):
    return num3 + num4

def cal_diff(num3, num4):
    return num3 - num4

def cal_prod(num3, num4):
    return num3 * num4

def cal_div(num3, num4):
    return num3 / num4

def cal_reminder(num3, num4):
    return num3 % num4

def cal_quotient(num3, num4):
    return num3 // num4

num3 = 10
num4 = 5

print('The sum of {} and {} : {}'.format(num3, num4, str(cal_sum(num3, num4))))
print('The diff of {} and {} : {}'.format(num3, num4, str(cal_diff(num3, num4))))
print('The prod of {} and {} : {}'.format(num3, num4, str(cal_prod(num3, num4))))
print('The div of {} and {} : {}'.format(num3, num4, str(cal_div(num3, num4))))
print('The reminder of {} and {} : {}'.format(num3, num4, str(cal_reminder(num3, num4))))
print('The quotient of {} and {} : {}'.format(num3, num4, str(cal_quotient(num3, num4))))


# part 3 << >>
print('\n')
print('PART 3-FORMAT3......convert.......to.....function....input...method...>>>>>')

def cal_sum(num5, num6):
    return num5 + num6

def cal_diff(num5, num6):
    return num5 - num6

def cal_prod(num5, num6):
    return num5 * num6

def cal_div(num5, num6):
    return num5 / num6

def cal_reminder(num5, num6):
    return num5 % num6

def cal_quotient(num5, num6):
    return num5 // num6

user_data_1 = input('Enter value for num5 : ')
user_data_2 = input('Enter value for num6 : ')


num5 = int(user_data_1)
num6 = int(user_data_2)

print('The sum of {} and {} : {}'.format(num5, num6, str(cal_sum(num5, num6))))
print('The diff of {} and {} : {}'.format(num5, num6, str(cal_diff(num5, num6))))
print('The prod of {} and {} : {}'.format(num5, num6, str(cal_prod(num5, num6))))
print('The div of {} and {} : {}'.format(num5, num6, str(cal_div(num5, num6))))
print('The reminder of {} and {} : {}'.format(num5, num6, str(cal_reminder(num5, num6))))
print('The quotient of {} and {} : {}'.format(num5, num6, str(cal_quotient(num5, num6))))



# part 4 using while True loop  << >>
print('\n')
print('PART 4-FORMAT4......convert.......to.....function...while..True.input...method...>>>>>')


def cal_sum(num7, num8):
    return num7 + num8


def cal_diff(num7, num8):
    return num7 - num8


def cal_prod(num7, num8):
    return num7 * num8


def cal_div(num7, num8):
    return num7 / num8


def cal_reminder(num7, num8):
    return num7 % num8


def cal_quotient(num7, num8):
    return num7 // num8


while True:
    user1 = input('Enter num7 :')
    if(user1.isdigit()):
        num7 = int(user1)
        break
    else:
        print('Please enter digit value !! ')

while True:
    user2 = input('Enter num8 :')
    if(user2.isdigit()):
        num8 = int(user2)
        break
    else:
        print('Please enter digit value !! ')


print('The sum of {} and {} : {}'.format(num7, num8, str(cal_sum(num7, num8))))
print('The diff of {} and {} : {}'.format(num7, num8, str(cal_diff(num7, num8))))
print('The prod of {} and {} : {}'.format(num7, num8, str(cal_prod(num7, num8))))
print('The div of {} and {} : {}'.format(num7, num8, str(cal_div(num7, num8))))
print('The reminder of {} and {} : {}'.format(num7, num8, str(cal_reminder(num7, num8))))
print('The quotient of {} and {} : {}'.format(num7, num8, str(cal_quotient(num7, num8))))

