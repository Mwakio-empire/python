class Person:
  def __init__(self, firstname, age, gender):
    self.firstname =firstname
    self.age = age
    self.gender = gender

  def details(self):
    print(self.firstname, "is studying")

Teacher = Person("Joe", 56, "male")
Accountant = Person("Mary", 26, "female")
Doctor = Person("John", 36, "male")

print(Teacher.firstname)

Doctor.details()
