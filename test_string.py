

# A String is a sequence of character << >>

string1 = 'Nwoye'
string2 = "Emeka"
string3 = '''Eleazar'''
string4 = """Home"""
string5 = '''Welcome
to
python learning '''

string6 = """Welcome
to
python learning """

print('str1 :', string1)
print('str2 :', string2)
print('str3 :', string3)
print('str4 :', string4)
print('str5 :', string5)
print('str6 :', string6)

print('\n')

string7 = 'Eleazar'\
          'is'\
          'good'\
          'man'\

print('String using backslash '.center(50, ('-')))
print('str7 :', string7)


string8 = ('Emeka'
          'loves'
          'vivian'
          'best'
           'in'
           'my'
           'heart' )

print('String using () '.center(50, ('-')))
print('str8 :', string8)

print('\n')

# printing string character index and range << >>

string9 = 'I love vivian because she is damn fine and a good girl'

print('1st character :', string9[0])
print('2nd character :', string9[1])
print('last character :', string9[-1])
print('8th - 18th character :', string9[7:18])
print('8th - 3rd in last character :', string9[7:-2])

# string operator << >>

print('\n')
print('String operators '.center(50, ('-')))

print('TYPE1 :')
me1 = 'I'
me2 = 'love'
me3 = 'vivian'

print('opt1 :', me1 + me2 + me3)
print('opt2 :', me1 + '',  me2 + '', me3)

print('TYPE2 :')

vee = me1
vee += ' '
vee += me2
vee += ' '
vee += me3
print(vee)

print('TYPE3 :')

print('>>', (me1 + ' ' + me2 + ' ' + me3 + ' ' ) * 5)

print('\n')
print('String iteration '.center(50, ('-')))

for char in 'Vivian':
    print(char)
print('String membership '.center(50, ('-')))
vee2 = 'vivian'

print('vivian in vee2 ?', 'vivian' in vee2)

print('String len '.center(50, ('-')))
print('vee2_length :',len(vee2))

print('String for lower/upper case. Title/is. startwith/endwith. lstrip/rstrip/strip '.center(150, ('-')))

name1 = 'JOY'
name2 = 'Emeka'
name3 = 'peace efe'
name4 =  '  good'
name5 = '12345'
name6 = 'bad  '
name7 = '   very    '


print('Low case :', name1.lower())
print('Upper case :', name2.upper())
print('Title :', name3.title())
print('name1 is alpha :', name1.isalpha() )
print('name2 is lower :', name2.islower() )
print('name5 is digit :', name5.isdigit() )
print('name1 starts with (J) ?', name1.startswith('J') )
print('name2 ends with (a) ?', name2.endswith('a') )
print('name4 lstrip :', name4.lstrip() )
print('name6 rstrip :', name6.rstrip() )
print('name7 strip both :', name7.strip() )

print('String for justify '.center(50, ('-')))

# string justify << >>
print('Flight to Abuja :'.ljust(20) + ' ', 'Time: 11:12am '  )
print('Flight to Lagos :'.ljust(20) + ' ', 'Time: 01:23pm '  )
print('Flight to Delta :'.ljust(20) + ' ', 'Time: 03:00pm '  )

# string for replace old and new << >>

print('String for replace '.center(50, ('-')))
ip_address1 = '10-10.0.0'
ip_address2 = '     10-10.0.0'
ip_address3 = '10-10.0.0    '

ip_address1 = (ip_address1.replace('-', '.'))
ip_address2 = (ip_address2.replace('-', '.')) .strip()
ip_address3 = (ip_address3.replace('-', '.')) .strip()
print(ip_address1)
print(ip_address2)
print(ip_address3)

print('String for split '.center(50, ('-')))

exmp_1 = 'A man is an anima'
exmp_2 = 'Aug-19-24|Broadstreet|gate1'

ext = exmp_1.split()
ext2 = exmp_2.split('|')
ext3 = exmp_2.split('|', 1)

print('Just split :',ext)
print('Split by delimiter :',ext2)
print('Split by delimiter and num of split :',ext3)

print('String for join '.center(50, ('-')))

exmp_3 = 'A man is an anima'
exmp_3 = '.'.join(exmp_3)
exmp_5 = ['A', 'man', 'is', 'an', 'anima']
exmp_5 = '| '.join(exmp_5)

print(exmp_3)
print(exmp_5)

sms = "it is urgent!"

print("  ".join(sms))
