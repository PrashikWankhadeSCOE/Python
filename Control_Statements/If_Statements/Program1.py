"""
if(condition):
    statements inside if
statements out of if 
"""

x = int(input("Enter the value of x : "))

if(x>18):
    print("Cheers !! You are eligible to vote ")
    # if here we dont give the tab
    # IndentationError : expected an indented block

print("Out of if")

'''
Enter the value of x : 29
Cheers !! You are eligible to vote
Out of if

Enter the value of x : 15
Out of if
'''

# If you want to write the condition but dont want to give any result on being true 
# In python it is compulsary to write something is the if block 
# so we can write pass statement so that it wont trow any error 
# If we keep the if block empty it will give us IndentationError : Expected an Indented Block

if(x<18):
    pass
print("Out of if")


# If we dont give the colon after if condition it will be a SyntaxError
# Colon is used to declare the block in python

if(x):
    print("true")

# in python every number except 0 is considered as true 
# as it is cpython internally it calls funtions of c so it acts like c

