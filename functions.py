def welcome(name):
  print("welcome" + name)


def add_numbers(num1, num2):
  print(num1,num2)
  return num1 + num2

def num_dividedFrom_add_numbers(num,addedNum):
  return num/addedNum

# def function():
#   pass
  

  
#   Create Functions Practice #1
  # Declare a function called greet, which every time it is called prints "Hello world!"

def greet(greeting):
  print("Hellow world!")
  
  # You should only define the function, you should not call it later.




########################################################################################################################
# Create Functions Practice #2
# Declare a function called welcome, which takes a person's name as an argument, and every time it is called, it prints "Welcome {name}!"

def welcome(name):
  print("welcome" + name)

# Create the variable name, and store any name inside of it, so we can test the function with a name of your choosing.
name = welcome("Melanie")

# You should only define the function and create the variable, you should not call the function afterwards.



########################################################################################################################
# Create Functions Practice #3
# Declare a function called square, that takes any number as an argument, and each time it is called, it prints the square of that number on the screen (that is, the value to the second power).
def square(num):
  print(num**2)
num = square(5)
# The name of the argument that this function must take is number. Create this variable and assign it any number.

# You should only define the function and create the variable, you should not call the function afterwards.