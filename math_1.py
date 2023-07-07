import random

"""
Add and substract negative numbers
"""

with open('output.txt', 'w') as f:
    f.write("Integers double digit - +\n")
    for i in range(10):
        x = '{:d}'.format(random.randint(5,35))
        y = '{:d}'.format(random.randint(55,99))
        f.write(x+" - "+y)
        f.write('\n')
    for i in range(10):
        x = '{:d}'.format(random.randint(5,39)*-1)
        y = '{:d}'.format(random.randint(45,89))
        f.write(x+" + "+y)
        f.write('\n')
    
    f.write("What patterns did you observe?\n\n")

    f.write("Integers double digit - -\n")
    for i in range(20):
        x = '{:d}'.format(random.randint(5,99)*-1)
        y = '{:d}'.format(random.randint(5,99))
        f.write(x+" - "+y)
        f.write('\n')
    
    f.write("What patterns did you observe?\n\n")

    f.write("Let's try something harder\n")
    f.write("Decimal single digit - +\n")

    for i in range(20):
        x = "{:.2f}".format(random.uniform(0,-9))
        y = "{:.2f}".format(random.uniform(0,9))
        f.write(x+" + "+y)
        f.write('\n')

    f.write("decimal double digit - +\n")

    for i in range(20):
        x = "{:.2f}".format(random.uniform(-10,-55))
        y = "{:.2f}".format(random.uniform(10,55))
        f.write(x+" + "+y)
        f.write('\n')


