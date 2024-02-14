temperature = 13

if temperature > 25 :
   print("It is Hot")
else:
 print("It is Cold")

# A program that returns the largest Number among three Numbers
num1 = 45
num2 = 56
num3 = 21
if num1 > num2 and num1 > num3:
  print(num1, "is the Largest number")
elif num2 > num1 and num2 > num3:
  print(num2, "is the largest number")
else:
  print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 0
if number % 2 == 0:
  print(number, "even")
else:
  print(number,"odd")

# A program that checks whether a number is a prime number or not
no = 4
if no > 1:
  for i in range(2, int( no/2)+1):
    if no % i ==0:
     print(no," is not a prime number")
     break
  else:
    print(no,"is a prime number")
else:
  print(no,"is not a prime number")




