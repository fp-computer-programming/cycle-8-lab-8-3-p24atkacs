"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-3.py
Write the while-loop version of the following for-loop program.

def sum_to(n):
  total = 0
	for i in range(n+1):
		total += i
	return total

The function should be able to have an integer passed to it and return the sum of all the values from 1 to that integer
"""

# Author: Andrew Tkacs

def sum_to(n):
    # Initialize total to store the sum
    total = 0
    
    # Initialize the loop variable
    i = 1
    
    # Use a while from 1 to n
    while i <= n:
        total += i  # Add the current value to the total
        i += 1
    
    # Return the final sum
    return total

result = sum_to(5)
print(f"Sum from 1 to 5: {result}")
