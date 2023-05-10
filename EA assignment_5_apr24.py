# -*- coding: utf-8 -*-

# -- Sheet --

list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 

x="data science"
y="machine learning"
z="edukron"

Write a Python program that takes the strings "x", "y", and "z", and concatenates them into a single string.

x+","+ y+","+ z

Write a Python program that takes the string "x" and replaces all occurrences of the letter "a" with the letter "e".

x="data science"
y="machine learning"
z="edukron"
  
# replace "top" with "top 1%"
print(x.replace("a", "e"))
 
# printing the original string

Write a Python program that takes the string "y" and removes all occurrences of the word "learning".

print(y.replace("learning","-"))

#Write a Python program that takes the string "z" and counts how many times each letter appears in the string.

x="data science"
y="machine learning"
z="edukron"

myset=set(x)


for unique_elements in myset:
    countOfChar = 0
    for character in x:
        if character == unique_elements:
            countOfChar += 1
    print("Count of character '{}' is {}".format(unique_elements, countOfChar))




Write a Python program that takes the string "x" and creates a new string where each word is capitalized.

x.upper()

Write a Python program that takes the string "z" and counts how many times each letter appears in the string.

#Write a Python program that takes the string "z" and counts how many times each letter appears in the string.

x="data science"
y="machine learning"
z="edukron"

myset=set(z)


for unique_elements in myset:
    countOfChar = 0
    for character in z:
        if character == unique_elements:
            countOfChar += 1
    print("Count of character '{}' is {}".format(unique_elements, countOfChar))




Write a Python program that takes the string "y" and creates a new string where each word is reversed.

x="data science"
y="machine learning"
z="edukron"
y[::-1]

Write a Python program that takes the string "z" and creates a new string where each word is sorted alphabetically.

sorted(z)

Write a Python program that takes the string "x" and creates a new string where each letter is replaced with its corresponding ASCII code.


for i in x:
    print("the ascii value of {0} is :{1}" .format(i, ord(i)))
#ord('a')

Write a Python program that takes the string "y" and creates a new string where each letter is replaced with the next letter in the alphabet.

x
for i in range(len(x)):
    i=(i+1)%(len(x))
   
    print(x[i])



Write a Python program that takes the string "z" and creates a new string where each letter is replaced with the letter that is three positions to the right in the alphabet.

print(z)
count=0
for i in range(len(z)):
    
    i=(count+3)%(len(z)) 
    count+=3
    print(z[i],count)


Write a Python program that takes the string "x" and creates a new string where each word is replaced with its length.


strg=x.split(" ")
for i in range(len(strg)):
    word1=len(strg[0])
    word2=len(strg[1])
print(str(word1),str(word2))



        

Write a Python program that takes the string "y" and creates a new string where each word is replaced with the number of vowels it contains.

print(y)
a=""
strg=y.split(" ")
for i in range(len(strg)):
    word1=strg[0]
    word2=strg[1]
    count_1=0
    count_2=0
    for i in word1:
        if i in 'aeiou':
            count_1+=1
#print(count_1)
    for i in word2:
        if i in 'aeiou':
            count_2+=1
print(count_1, count_2)



#     word2=len(strg[1])
# print(str(word1),str(word2))




Write a Python program that takes the string "z" and creates a new string where each word is replaced with its length, divided by the number of vowels it contains.

print(z)
a=""
len_z=len(z)
count=0
for i in z:
    
    #print(i)
    if i in 'aeiou':
        count+=1
print(len_z%count)




Write a Python program that takes the string "x" and creates a new string where each word is replaced with the reverse of its letters.

a=''
b=''
print("original string is {0}:".format(x))
strg=x.split(" ")
#print(strg)
for i in range(len(strg)):
    word1=strg[0]
    word2=strg[1]
print( word1, word2)
print(word1[::-1] , word2[::-1])
# for j in word1:
#     if 'e' in j:
#         a=word1[::-1]
# for j in word2:
#     if 'e' in j:
#         b=word2[::-1]
        
#print("reversed string is ", word1[::-1] , word2[::-1])

Write a Python program that takes the string "y" and creates a new string where each word is replaced with the reverse of its letters, but only if the word contains the letter "e".

x="data science"
y="machine learning"
z="edukron"

a=''
b=''
print("original string is {0}:".format(y))
strg=y.split(" ")
#print(strg)
for i in range(len(strg)):
    word1=strg[0]
    word2=strg[1]
for j in word1:
    if 'e' in j:
        a=word1[::-1]
for j in word2:
    if 'e' in j:
        b=word2[::-1]
        
print("reversed string is {0} and {1}:" .format(a, b))
  
    

   



