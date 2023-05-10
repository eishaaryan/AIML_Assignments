# -*- coding: utf-8 -*-

# -- Sheet --

# # What is the type of variable "a" in Python?


a=1
type(a)

# # What is the type of variable "b" in Python?




# # What is the type of variable "c" in Python?




# # Can the value of variable "a" be changed to a string? Why or why not?


b=str(a)
b

# # Can the value of variable "b" be changed to an integer? Why or why not?


x=int(b)
## can't done

# # Can the value of variable "c" be changed to a string? Why or why not?




# # How would you convert the value of variable "a" to a string?




# # How would you convert the value of variable "b" to an integer?


b=int(input())
b

# # How would you convert the value of variable "c" to a string?


c=str(12)
c

# # What is the real part of variable "c"?




# # What is the imaginary part of variable "c"?




# # How would you create a new variable "d" that is equal to the sum of variables "a" and "b"?


a=1
b=2
d=a+b
d

# # How would you create a new variable "e" that is equal to the difference between variables "b" and "a"?


e=b-a
e

# # How would you create a new variable "f" that is equal to the product of variables "a" and "b"?


f=a*b
f

# # How would you create a new variable "g" that is equal to the quotient of variables "b" and "a"?




# # How would you create a new variable "h" that is equal to the square of variable "a"?


a=4
h=a**2
h

# # How would you create a new variable "i" that is equal to the square root of variable "b"?


i=math.sqrt(b)
i

# # How would you create a new variable "j" that is equal to the absolute value of variable "e"?


j=abs(e)
j

# # How would you create a new variable "k" that is equal to the complex conjugate of variable "c"?


c=2+4j
import numpy
k=numpy.conj(c)
k

# # How would you create a new variable "l" that is equal to the modulus of variable "c"?


i=abs(c)%2
i

# # How would you compare the values of variables "a" and "b"?


a=1
b=2
if a==b:
    print(True)
else:
    print(False)

# # How would you compare the values of variables "b" and "c"?




# # How would you compare the values of variables "a" and "c"?




# # How would you round the value of variable "b" to the nearest integer?


b=2.3456789
round(b,1)

# # How would you round the value of variable "b" to two decimal places?


round(b,2)

# # How would you check if the value of variable "a" is an even number?


a=7
if a%2==0:
    print("evern number")
else:
    print("odd number")

# # How would you check if the value of variable "c" is a complex number?




# # How would you check if the value of variable "b" is greater than 20?


b=7
if b>20:
    print("True")
else:
    print("False")

# # How would you check if the value of variable "c" has a positive imaginary part?


c=2+3j
import numpy as np
if np.imag(c)>0:
    print(True)
else:
    print(False)

# # How would you check if the value of variable "a" is a non-zero number?


a=5
if a>0:
    print("non zero number")
else:
    print("equal to or less then zero")

# # How would you check if the value of variable "b" is a non-negative number?


a=5
if a>=0:
    print("non negative")
else:
    print("negative number")

# # How would you create a new variable "m" that is equal to the integer part of variable "b"?


b=2.33
m=int(2)
m

# # How would you create a new variable "n" that is equal to the fractional part of variable "b"?


b
m=b%2
round(m,2)

# # How would you create a new variable "o" that is equal to the minimum value of variables "a", "b", and "c"?


a=2
b=3
c=4
d=min(a,b,c)
d

# # How would you create a new variable "p" that is equal to the maximum value of variables "a", "b", and "c"?


a=2
b=3
c=4
d=max(a,b,c)
d

# # How would you create a new variable




