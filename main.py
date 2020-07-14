print("Williams")
number_of_doughnuts = 5
number_of_doughnuts ="f"
number_of_doughnuts = True
number_of_doughnuts = 5.5
print(number_of_doughnuts)
doughnut_name = "Glaze"
name = "Hello"
doughnut_name = "name"

print(doughnut_name)

Doughnut_exist = True
amount_of_food = 10
print(amount_of_food + number_of_doughnuts)

amount_of_food -= 1
amount_of_food = amount_of_food - 1
if number_of_doughnuts == 0:
 Doughnut_exist = False
elif number_of_doughnuts >=5:
  number_of_doughnuts -=1
else:
  number_of_doughnuts += 1

Life = 50
if Life == 0:
  print("you have died")
else:
  Life -= 1
print(Life)


print("create a username")
username = input("what is yourname:\n ")
age = input("Hello " + username+", how old are you?\n" )
if int(age)>12 and int(age)<99:
  print(username + "welcome to the site" )
elif int(age) <=12:
  print(username + "you are not old enough to view this site" )
else:
  print(username + "how are you even operating the computer" )

if int(age) >= 99:
  print("account invalid")
elif int(age) >= 13: # 100 > age >=13
  print("account active")
else:
  print("too young")


 

a=3
b=6
if a>b:
  print("a is greater than b")

x = 2 
print(x) 
if x > 3:
  x += 2
print(x)

has_key = True 
if has_key == True:
  print("You won! Unlock the door!") 

player_age = 22

if player_age >= 21:
  print("You could be a teacher")
elif player_age >= 18:
  print("You could be in college.")
elif player_age >= 13:
  print("You can also attend iD Academies!")
elif player_age >= 7:
  print("You can attend iD Tech Camps!")
else:
  print("You're young.")

player_has_item = True
score = 150
won = False

if player_has_item and score > 100:
    won = True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")


player_has_item = False
score = 202
won = False

if player_has_item or score > 200:
    won = True

if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")



x = 0

while x <= 10:
  print(x)
  x += 1