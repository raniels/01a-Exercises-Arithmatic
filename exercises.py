'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2
#20
35 / 5
#7.0

35 / 4
#8.75
35 // 4
#8
# What is the difference between the / operator and the // operator?
# The / operator divides and gives the exact value (if there is an exact value), while the // operator divides then rounds down to the nearest whole number.

2 ** 5
#32
# What does the ** operator do?
# The operator ** takes the the first number to the 2nd number's power. (So 2 ** 3 would be 2 * 2 * 2)
5 % 3
#2
5 % 2
#1
5 % 4
#1
# What does the % operator do?
# The % operator divides then outputs the remainder

(1 + 3) * 2
#8
# What effect do the parenthesis have on this statement?
#It makes it so that 1 and 3 are added first instead of 3 being multiplied by 2 then add 1. Order of operations.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
#<class 'int'>
type(3.0)
#<class 'float'>
type("word")
#<class 'str'>
type(True)
#<class 'bool'>
type(False)
#<class 'bool'>
type(None)
#<class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another.
int(3.0)
#3
float(7)
#7.0
str(55)
#'55'
bool(1)
#True
# How can you tell the difference between these four different types?
#Float gives a decimal, int gives an integer, str gives a string (is surrounded by ' '), while bool outputs true or fales

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
#It combines both strings and outputs them as one (ex. 'Helloworld')

"This is a string"[0]
#T
"This is a string"[5]
#i
"This is a string"[8]
#a
# What is happening as you change the number?
#It changes what character is given, where the number is the palce of the character with 0 being first, it also ignores spaces. So in this example changing the number to 3 would give you 's')

"This is a string"[-1]
#'g'
# What happens when you use a negative number?
#It starts from the end of the string

"%s can be %s" % ("strings", "interpolated")
# What is happening here?
#can be is being inserted in the string between strings and interpolated

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
#Hello, Python
# What just happened?
#After entering the input command it asked me to provde an input (what n would stand for), and after entering the 2nd line it replaced + n with my answer.

# For your next assignment, you will need to use random numbers
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# It is giving me random numbers.

randint(1,100)
# How is this different?
#It changed the range to 1 to 100 as well as forcing the answer to be an integer

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# It put the items in a random order, that does not change until you shuffle again.

print(sample(items, 1))
# What does this do?
# It gives me a random item

print(sample(items, 5))
# What does the second parameter control?
# The amount of items it will give me

for i in range(0,5):
	print(i)
#0
#1
#2
#3
#4
# What is happening here? What happens if you change the two range parameters?
#It is giving me the integers between the 2 parameters, including the first number, but not the last one. If I change the parameters it will give me the integers between those, including the first parameter, but not the last one.
