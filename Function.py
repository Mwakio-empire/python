# Inbuilt Functions
number = max(89,70,12,123,45)
print(number)

x = min(78,45,34,1)
print(x)

z = pow(2,3)
print(z)

# User-defined functions
def name():
  print("Bukayo")

name() # Calling a function

def student():
   name = "Takehiro"
   age = 19
   course = ("HTML")

   print(name,age,course)

student()


# Parameters/variables and arguments/value
def students(name,age,course):
  print(name,age,course)

students("Dedan",17,"MIT")
students("Mark",18,"Java")
students("Allan",18,"CSS")
students("Gabriel",18,"Cybersecurity")
students("Declan",24,"Python")


# Create a user defined function
def employees(Fullname,age,gender,position,salary):
  print(Fullname, age, gender, position, salary)
employees("Angel",19,"Male","CEO",500000)
employees("Declan",18,"Male","Secretary",400000)
employees("Sophia",16,"Female","Admin",300000)
employees("Darren",15,"Male","Holder",200000)
employees("Ivy",17,"Female","Cashier",100000)







