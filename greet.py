

# Define a function called *greet* that meets the following criteria: 
    # Takes an argument called *name*.
    # Prints a greeting using the *name* parameter.

def greet(name):
    print(name)

# Define another function called *name_input* that meets the following criteria:
    # Takes no arguments.
    # Prints a message to the screen requesting the user to provide a name.
    # Returns a string with the value equals to that of the provided name.   

def name_input():
  print("Please provide your name")
  name = input("Please enter your first name: ")
  return name 

# Using these two functions, prompt the user for a name and print it to the screen.

givenName = name_input()
print(givenName)