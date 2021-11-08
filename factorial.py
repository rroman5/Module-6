#Roberto Roman
#11/07/21

import math
#user enters number
fact = int(input("Enter number to compute to a factorial"))
#importing factorial to give answer
for i in range(1):
    number = math.factorial(fact)
    #print the answer with the factorial value
    print ("The value given", fact,"is", number)
