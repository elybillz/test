from itertools import count
from operator import truediv


name = "john"
print(name)
print("ely")
print("rita")

#for like border top
print("=============")

# allign inline
print("mary \t mose\t cy \t gift" )
print("=============")

#allign block
print(" corn \n mango \n apple")

print("hannah", " " "mother", sep=",", end=".")

#for line br
print("\n")

print("hannah", "mother", sep=",", end=".")

message = "start processing"
print(message)
print(message.center(50, "="))

#print using format
name = "eleazar"
city = "asaba"
work = "siemician"
print(name + " live in ", city + " and he works as a ", work )
print("{} live in {} and he works as a {}.".  format(name, city, work) )


#if condition
raining = True
score = 200
if raining:
 print("yes it is raining")
else:
    print("no is not raining")

print("-----------")

if score >= 300:
    print("score greater than 300")
else:
    print("score not greater than 300")

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
    print("requested ticket amount not available!")
    