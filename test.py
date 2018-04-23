from sys import argv
import random

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()


print "I'm going to write the file."


i = 0
while i < 1:
    
    from random import randint
    variable1 = randint(1,999)
    
    target.write("i = 0")
    target.write("\n")
    target.write("while i < 99:")
    target.write("\n\t\t")
    target.write("print 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis, odio non tempor pulvinar, quam nisl tempor risus, placerat pellentesque risus ipsum sit amet arcu.'")
    #target.write(str(variable1))
    target.write("\n\t\t")
    target.write("i = i + 1")
    
    i = i + 1

print "And finally, we close it."
target.close()

import test2


#to run: python test.py test2.py

