# Define a function named *exponentiate* with the following criteria:
    # Takes two integers as arguments.
    # Returns the value of the first integer raised to the power of the second integer.

def exponentiate(base, exponent):
    return base ** exponent  

# Define a function named *raise_to_fourth_power* with the following criteria:
    # Takes one integer as an argument.
    # Calls the *exponentiate* function to raise the given paremeter to the 4th power.

def raise_to_fourth_power(number):
  return exponentiate(number, 4)

# Create a variable called *square*. The value assigned to this variable should be a lambda expression
# that utilizes the *exponentiate* function to raise a number to the power of 2.

square = lambda x: exponentiate(x, 2)

# Create a variable called *cube*. The value assigned to this variable should be a lambda expression 
# that utilizes the *exponentiate* function to raise a number to the power of 3.

cube = lambda x: exponentiate(x, 3)

# In the main part of the script print the output of square(2), cube(2), raise_to_fourth_power(2).

print(square(2))  
print(cube(2))   
print(raise_to_fourth_power(2))  

# When executed, your script should provide the following output. 
#4   
#8   
#16  
