#Roberto Roman
#11/07/21

import random

print ("This is the following random integer between 25 and 35")

for i in range (10): #<--- In here we have the order
    num = random.randrange (25, 35)
    print (num, end= ' ')