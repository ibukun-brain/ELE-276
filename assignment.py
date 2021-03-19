import turtle
import time 

# ================================================================================================
# SOLUTION NO: 1
# This algorithm can be use to create a circle within a circle(10 circles) using python turtle
# ================================================================================================

"""The idea behind the solution is a simple math, start the coordinate of the turtle from (0,0). 
any size of the circle is allowed. The trick to solving this problem is to increase the y axis 
by any number and subtract from the radius of the circle. in this case i started the origin(0,0) 
and used a circle radius of 100, after that i increase the y axis by 5 and subtract it from intial 
radius which is 100 and so on. In order to make the circles within the circle uniform"""

circle_radius = 100
for i in range(0, circle_radius, 5):
    turtle.color('black')
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
    turtle.circle(circle_radius - i)
    if i == 45:
        break
    
turtle.hideturtle()
turtle.done()


# ========================================================================================
# SOLUTION NO: 2
# 
# ========================================================================================

print('This algorithm can be use to return the character of an ASCII code')
user_input = int(input('Enter an ASCII code(from 0 to 127): '))

if user_input >127 or user_input < 0:
	print('Number is out of range, Try again!.')
	
else:
	print('The Character is', chr(user_input))
    
print('\n')
print('#','='*90)
print('\n')


# ========================================================================================
# SOLUTION NO: 3
# This program can be use for determining the solution of a quadratic equation
# ========================================================================================

import cmath #for complex mathematical operations

print('Welcome to Quadratic equation solver')
time.sleep(3) #For interactiveness
a, b ,c = eval(input('Enter the value of a,b,c: ')) #prompts the user to input the values of a,b and c respectively

if a == 1: #if the coefficient of x^2 = 1 then return x^2 instead of 1x^2
    print('Quadratic Equation = x^2 + {}x + {}'.format(a, b, c))
else:
    print('Quadratic Equation = x^2 + {}x + {}'.format(a, b, c))

d = cmath.sqrt(b**2 - 4*a*c) 

m1 = (b + d)/2*a
m2 = (-b - d)/2*a

print('The root of the equations are {} and {} respectively.'.format(m1,m2))

print('\n')
print('#','='*90)
print('\n')


# =====================================================================================================================
# SOLUTION NO: 4
# This program can be use to solve any 2 x 2 Linear Algebra Equation using cramer's rule
# =====================================================================================================================
'''Initially the line of code comment below would have work but if the denominator (a*d -b*c) = 0 an error will 
   occur which is called (ZeroDivisionError), ZeroDivisionError occurs when the numerator is divided by zero(0). 
   This can be fix by catching the error and making an exception for this error using try and except '''
   
# a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: ')) #prompts user to input the values of a,b,c,d,e and respectively
# x = (e*d - b*f) / (a*d - b*c) # formula for x
# y = (a*f - e*c) / (a*d - b*c) # formula for y

# print('x is {} ,y is {}'.format(x,y)) # print the answer for both x and y
# ================================================================================================================
import time # importing time to make the program a little bit interactive

print('Welcome to the 2 x 2 Linear Algebra Equation Solver')
time.sleep(3) # delays the next line of code for a 3 seconds
print("This program can be use to solve any 2 x 2 Linear Algebra Equation using cramer's rule")

'''The try and except statement used here to make an exception for the ZeroDivisionError i.e instead of having 
ZeroDivisionError when the numerator is divided by the denominator(i.e when (a*d -b*c) = 0) , 
we have the "The Equation has no solution'''

try:
    a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    print('x is {} ,y is {}'.format(x,y))

except ZeroDivisionError:
	print('The equation has no solution')
    
print('\n')
print('#','='*90)
print('\n')

# =====================================================================================================================
# SOLUTION NO: 5
# This program can be use to display the name of the day of the week by prompting the user to enter the year, month 
# and day of the month 
# =====================================================================================================================

print('This program can be use to display the name of the day of the week')
time.sleep(2)

k = eval(input('Enter year: (e.g., 2008): ')) # prompts the user to enter the year
m = eval(input('Enter month: 1-12: ')) # prompts the user to enter the month
q = eval(input('Enter the day of the month: 1-31 : ')) # prompts the user to enter the day of the month
j = k

'''(Hint: for a positive n. January and February are counted as 13 and 14 in the formula, so you need to
    convert the user input 1 to 13 and 2 to 14 for the month and change the year to the previous year.)'''
if m == 1: #converts the user input 1 to 13
    m = 13
    
elif m == 2: #converts the user input 2 to 14
    m = 14
    
else:
    k = k - 1 #change the year to to the previous year
    j = j - 1
    pass
    
h = (q + ((26*(m + 1))//10) + k + (k//4) + (j//4) + 5*j) % 7 #formula for Zeller's Congruence

# print(h)
days_of_the_weeks = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
print('Day of the week is', days_of_the_weeks[h])