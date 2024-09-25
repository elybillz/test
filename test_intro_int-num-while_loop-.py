



# numbers e.g. integer, boolean, float, complex numbers << >>>
# for var_sum / input int & float <<< >>>


var_integer = 8
var_float = 6.5

var_sum = var_integer + var_float

print ("Var_integer: ", type(var_integer))


var_num1 = input("enter num1 :")
var_num2 = input("enter num2 : ")

var_sum = int(var_num1) + float(var_num2)

print("var_num1 data type : ", type(var_num1))
print("var_num2 data type : ", type(var_num2))

print("value of var_sum", var_sum)
print("var_sum data type :", type(var_sum))


print('end and cnt'.center(50, ('_')))

name = "john"
print(name)
print("ely")
print("rita")

#for like border top <<< >>>
print("=============")

# allign inline <<< >>>
print("mary \t mose\t cy \t gift" )
print("=============")

#allign block <<< >>>
print(" corn \n mango \n apple")

print("hannah", " " "mother", sep=",", end=".")

#for line br <<< >>>
print("\n")

print("hannah", "mother", sep=",", end=".")

message = "start processing"
print(message)
print(message.center(50, "="))

#print using format <<< >>>
name = "eleazar"
city = "asaba"
work = "siemician"
print(name + " live in ", city + " and he works as a ", work )
print("{} live in {} and he works as a {}.".  format(name, city, work) )


#if condition <<< >>>
raining = True
score = 200
if raining:
 print("yes it is raining")
else:
    print("no is not raining")

print("-----------")

# if condition for score <<< >>>
if score >= 300:
    print("score greater than 300")
else:
    print("score not greater than 300")

# if condition for  input movies wit elif <<< >>>
movie1_tickets_available = 3
movie2_tickets_available = 5
movie3_tickets_available = 8

movie_selected = input('which moive package do you want? :')
count = input('pls select numbers of ticket ')
if movie_selected == "movie1" and int(count) <= movie1_tickets_available:
    print("here are your tickets - {}".format(movie_selected))

elif movie_selected == "movie2" and int(count) <= movie2_tickets_available:
    print("here are your tickets - {}".format(movie_selected))

elif movie_selected == "movie3" and int(count) <= movie3_tickets_available:
    print("here are your tickets - {}".format(movie_selected))
else:
    print("requested ticket amount not available or wrong input!")


print(".......print..........")



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



