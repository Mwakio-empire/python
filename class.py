# class is a blueprint of an object
# an object is an instance of a class

class Person:
  # Properties/attributes/characteristics
  name = "Bob"
  age = 23
  location = ("Westlands")

  def speak (self):
    print("Person is speaking")

accountant = Person()  # instantiating an object
print(accountant.age)

accountant.speak()
