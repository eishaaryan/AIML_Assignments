# -*- coding: utf-8 -*-

# -- Sheet --

# # How would you concatenate the values of variables "a" and "b" into a single string?


a="machine"
b="learning"
strg1=a+b
strg1

# # How would you slice the first two characters from variable "a"?


a[:2]

# # How would you slice the last two characters from variable "b"?


b[:2]

# # How would you capitalize the first letter of variable "a"?


a.capitalize()

# # How would you swap the case of all letters in variable "b"?


b.swapcase()

# # How would you replace the substring "machine" with "deep" in variable "a"?


for i in a:
    x=a.replace("machine","deep")
print(x)

# # How would you count the number of occurrences of the letter "e" in variable "b"?


count=0
for i in b:
    if i=='e':
        count+=1
print(count)

# # How would you split the string in variable "a" into a list of words?


a="Deep Learning"
a.split(" ")

# # How would you reverse the order of characters in variable "b"?


b[::-1]

# # How would you check if variable "a" contains only alphabetic characters?


a.isalpha()

# # How would you check if variable "b" contains only numeric characters


b.isnumeric()

# # How would you remove all whitespace characters from variable "a"?


a.replace(" ","")

# # How would you pad variable "b" with zeros to make it a string of length 7?


b.center(10,'0')

# # How would you create a dictionary that maps each word in variable "a" to its length?


strg=a.split(" ")
print(strg)
for i in range(len(strg)):
    word1=strg[0]
    word2=strg[1]
    word1_l=len(strg[0])
    word2_l=len(strg[1])
print(word1, word2)
    
print(word1_l,  word2_l)

{v:k for k,v in enumerate(strg)}





