## Quadratic Eq. Solver


## TODO: FIX THE ERRORZ
## TODO: After finishing, we can make the script accomodate complex roots. For extra credit.

from math import *


class QuadEq:
    """A class that defines a quadratic equation to find the real roots of quadratic function."""
    values = []

    def quadraticSolver(self, a, b, c):
        answer = []
        ## if (b**2 - 4*a*c) aka the discriminant is negative, then math domain error
        x = -b + sqrt(b**2 - 4*a*c)  
        x = x/float(2*a)
        answer.append(x)
        x2 = -b - sqrt(b**2 - 4*a*c)
        x2 = x2/float(2*a)
        answer.append(x2)    
        print 'Answer(s): \n', answer
        return answer
    
    def negDiscriminant(self, a, b, c):
        if (b**2 - 4*a*c) < 0:
            return True
        else:
            pass   ## do nothing



def numberInput():
    equation = QuadEq()

    for value in ('a','b','c'):
        print 'Please provide the value of ', value
        var = raw_input('> ') 
        var = float(var)
        setattr(equation, value, var)

    print equation.a, ' is the value assigned to \'a\' on the fly with setattr()'
    print equation.b,  ' is the value assigned to \'b\' on the fly with setattr()'
    print equation.c, ' is the value assigned to \'c\' on the fly with setattr()'

    print 'Calculating...'

    cat = equation.a
    dog = equation.b
    pig = equation.c

    ## neg_test will be either True or False
    neg_test = equation.negDiscriminant(cat, dog, pig)

    if neg_test == True:        # gotta use double equals to test for equality, single equal is variable assignment
        print 'Your discriminant is negative. Please try again.'
        numberInput()
    else:
        ## pass these assigned variables to quadraticSolver(). The first-order argument 'self' is passed automatically.
        equation.quadraticSolver(cat, dog, pig)




def discCheck(a, b, c):
    if (b**2 - 4*a*c) < 0:
        print 'Please enter stuff that won\'t mess things up'
        loopexit = False
        return loopexit
    else:
        loopexit = True
        return loopexit


loopexit = False
print 'Entering while loop...'
while loopexit == False:  ## must use double equals to test for equality

    numberInput()
    loopexit == True

print 'ending'



