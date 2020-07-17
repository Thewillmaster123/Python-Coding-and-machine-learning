class MyPet:
  def __init__(self,pet_species, pet_name, pet_age):
    self.species =pet_species
    self.name = pet_name
    self.age = pet_age

  



class Alien:
  def __init__(self,Alien_species, Alien_name, num_arms):
    self.species =Alien_species
    self.name = Alien_name
    self.arms = int(num_arms)

  def high_five(self):
    for x in range(0,self.arms):
      print(self.name + "gives you a high five")

Blue_Alien = Alien("Green_Alien","josh", 2 )
print(Blue_Alien.name)
Blue_Alien.high_five()

class Human(Alien):
  def __init__(self,human_name,region_lived_in):
    self.name =human_name
    self.species = "Human"
    self.arms = 2
    self.region = region_lived_in

  def talk(self,speech):
    print(speech)

Jeff = Human("jeff","united States")
Jeff.talk("Hello,I'm Jeff")

class Dog(MyPet):
  def __init__(self, dog_age, dog_name):
    self.species = "dog"
    self.age = dog_age
    self.name = dog_name


  def play_fetch(self):
   print("Your pet" + self.name + "seems happy to play fetch")

Ralph = Dog(2,"Ralph")
Ralph.play_fetch()







    