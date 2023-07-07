import random

"""
Add and subtract fractions
"""

with open('output2.txt', 'w') as f:
    f.write("Single digit fraction\n")
    for i in range(10):
        x = '{:d}'.format(random.randint(1,9))
        y = '{:d}'.format(random.randint(2,9))
        a = '{:d}'.format(random.randint(1,9))
        b = '{:d}'.format(random.randint(2,9))
        f.write(x+"/"+y +" - " +a+"/"+b)
        f.write('\n')

    for i in range(10):
        x = '{:d}'.format(random.randint(1,9))
        y = '{:d}'.format(random.randint(2,9))
        a = '{:d}'.format(random.randint(1,9))
        b = '{:d}'.format(random.randint(2,9))
        f.write("-"+x+"/"+y +" + " +a+"/"+b)
        f.write('\n')

    f.write("\nDouble digit fraction\n")
    for i in range(10):
        x = '{:d}'.format(random.randint(1,99))
        y = '{:d}'.format(random.randint(2,99))
        a = '{:d}'.format(random.randint(1,99))
        b = '{:d}'.format(random.randint(2,99))
        f.write(x+"/"+y +" - " +a+"/"+b)
        f.write('\n')

    for i in range(10):
        x = '{:d}'.format(random.randint(1,99))
        y = '{:d}'.format(random.randint(2,99))
        a = '{:d}'.format(random.randint(1,99))
        b = '{:d}'.format(random.randint(2,99))
        f.write("-"+x+"/"+y +" + " +a+"/"+b)
        f.write('\n')

    
    f.write("\nMix of add and subtract negative integers and fractions\n")
    
    for i in range(20):
        num_terms = random.randint(2,4)
        """
        type 1: positive integer
        type 2: negative integer
        type 3: positive fraction
        type 4: negative fraction
        """
        for t in range(num_terms):
            type_cal = random.randint(1,4)
            match type_cal:
                case 1:
                    f.write("+"+'{:d}'.format(random.randint(1,99)))
                case 2:
                    f.write('{:d}'.format(random.randint(1,99)*-1))
                case 3:
                    a = '{:d}'.format(random.randint(1,99))
                    b = '{:d}'.format(random.randint(2,99))
                    f.write("+"+a+"/"+b)
                case 4:
                    a = '{:d}'.format(random.randint(1,99)*-1)
                    b = '{:d}'.format(random.randint(2,99))
                    f.write(a+"/"+b)
        f.write("\n")
        
            
