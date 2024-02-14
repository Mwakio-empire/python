# Parent class
class Animal:
  def speak(self):
    print("Animal is speaking")

# Child class
class Dog(Animal):
  def bark(self):
    print("Dog is barking")

class cat(Dog):
  def meow(self):
    print("cat is meowing")

a = Animal()
d = Dog()

c = cat()
