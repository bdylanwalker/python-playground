print "Welcome to Codecademy's Python Course!"

# VARIABLES

my_variable = 10

my_int = 7
my_float = 1.23
my_bool = True

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int


# WHITESPACE

def spam():
    eggs = 12
    return eggs


print spam()

spam = True
eggs = False

# this is a single line comment

mysterious_variable = 42


"""This
is a
multiline
comment
"""


# MATH

# Set count_to equal to the sum of two big numbers

addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9

count_to = 5000 + 10000

print count_to


# Set eggs equal to 100 using exponentiation on line 3!

eggs = 10 ** 2

print eggs

#Set spam equal to 1 using modulo on line 3!

spam = 3 % 2

print spam

# This is a single line comment
monty = True
python = 1.234
monty_python = python ** 2


# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)


# STRINGS

# Set the variable brian on line 3!

brian = "Hello life!"

# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"


# Put your variables above this line

print caesar
print praline
print viking

# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

parrot = "Norwegian Blue"

print len(parrot)
print parrot.lower()
print parrot.upper()

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

"""Tell Python to print "Monty Python"
to the console on line 4!"""

print "Monty Python"

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

# Print the concatenation of "Spam and eggs" on line 3!

print "Spam " + "and " + "eggs"

# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
    "and your favorite color is %s." % (name, quest, color)

# Write your code below, starting on line 3!

my_string = "This is my string"
print len(my_string)
print my_string.upper()


