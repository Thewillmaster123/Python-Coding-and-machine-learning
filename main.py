import random

rand_num = random.randint(1,3)

if rand_num == 1:
  print("low roll")
elif rand_num ==2:
  print("average")
else:
  print("high roll")

def random_number(max_int):
  rand = random.randint(0,max_int)
  return(rand)


num = random_number(100)
print(num)

def roll ():#function decleration
  roll_value = random.randint(1,20)#fuction body
  return(roll_value)#function body

my_roll = roll()
if my_roll == 1:
  print("sucks to suck")
elif my_roll <=10:
  print("something average")
elif my_roll < 20:
  print("something good")
else:
  print("you are the the bomb")

def roll2():
  roll_value = random.randint(1,20)
  if my_roll == 1:
   return "not so bad"
  elif my_roll ==10:
   return "something average"
  elif my_roll < 20:
    return "something good"
  else:
    return "you won the loterry"

text = roll2()












x = 0

while x <= 10:
  print(x)
  x += 1

num_to_guess = 50
num_attempt = 1
guess = int(input("pick number between 0 and 100: "))

while not num_to_guess == guess:
  if guess > num_to_guess:#the condition
    guess = int(input("Too High.Guess Again"))#loop body
  elif guess < num_to_guess:
    guess = int(input("Too Low. Guess Again"))
  num_attempt += 1

print("you got it right" + str(num_attempt) + "attempts") 

num_viruses = 15

for x in range(0,num_viruses):
  print(str(x) + "viruses have been deleted")


num_outputs = int(input("any number"))
num_divisible = int(input("any number i should test"))



for x in range(1, num_outputs + 1 ):
  print (x * num_divisible )

