from itertools import count
from operator import truediv


# if condition for score wit elif <<< >>>
score = 99
if score < 100:
    print("score lesser than 100")
elif score == 100:
    print("score is equal to 100")
elif score > 100:
    print("score is greater than 100")

print("---------------")

# while condition for loop <<< >>>
x = 0
while x <= 10:
    print('i am inside the loop : ' + str(x))
    print('>>>> incremented to ' + str(x))
    x += 1
    if x == 3:
        print('found : 3 ')
        continue

print('<<< This is the value of X >>> ')

#  the "for" loop condition <<< >>>
print('--------------------------------------------')
for x in "ely", "billz", "is", "a", "tech", "bro":
        print('>>> ' + str(x))

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
