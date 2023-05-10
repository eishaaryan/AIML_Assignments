# -*- coding: utf-8 -*-

# -- Sheet --

x = "Data Science"
y = "Edukron"
z = "Machine Learning"

# # How would you convert the string x to lowercase letters?


x.lower()
x

# # How would you convert the string y to uppercase letters?


y.upper()
y

# # How would you capitalize the first letter of the string z?


z[0]

# # How would you check if the string x contains the word "data"?


for i in range(len(x)):
    if x[i]=='data':
        print('True')
        break
    else:
        print('False')

# # How would you replace the word "Science" in the string x with "Analytics"?


x = "Data Science"

y = x.replace("Science", "Analytics")

print(y)

# # How would you split the string y at each occurrence of the letter "r"?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"

txt=y.split("r")
txt

# # How would you remove any leading or trailing spaces from the string z?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"

txt=z[1:-1]
txt

# # How would you concatenate the strings x, y, and z into one string?


txt=x+","+y+","+z
txt

# # How would you check if the string y ends with the letter "n"?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"

for i in range(len(y)):
    if y[-1]=='n':
        print("True")
        break
    else:
        print("false")


# # How would you get the length of the string x?


print(len(x))

# # How would you count the number of occurrences of the letter "a" in the string z?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
for i in range(len(z)):
    if z[i]=='a':
        count+=1
print(count)

# # How would you check if the string y is entirely composed of alphabetic characters?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
for i in range(len(z)):
    if z[i].isalpha():
        print("True")
        break
    else:
        print("False")

# # How would you center the string x in a string of length 20 with "-" as the padding character?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
x.center(20,"-")

# # How would you check if the string z starts with the word "Machine"?


z = "Machine Learning"
if z.startswith("Machine"):
    print("True")
    
else:
    print("False")

# # How would you encode the string y using the UTF-8 encoding?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
for i in range(len(z)):
    if z[i].isalpha():
        print("True")
        break
    else:
        print("False")

# # How would you find the position of the first occurrence of the letter "a" in the string x?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
for i in range(len(x)):
    if z[i]=='a':
        count+=1
    print(i)

# # How would you format the string z with the variable x using the format() function?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
# z = "For only {price:.2f} dollars!"
print("Machine Learnig is {0}".format(x))

# # How would you join the strings x, y, and z into one string separated by a comma?


str_1=x+","+y+","+z
str_1

# # How would you check if the string z is entirely composed of numeric characters?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
for i in range(len(z)):
    if z[i].isnumeric():
        print("True")
        break
    else:
        print("False")

# # How would you replace all occurrences of the word "Learning" in the string z with "Algorithms"?




y = z.replace("Learning", "Algorithms")

print(y)

# # How would you strip all vowels from the string x?


print(x)
for i in x:
    if i not in 'aeiou':
        print(i)

# # How would you left-justify the string z in a string of length 15 with "#" as the padding character?



print(z.rjust(15, "#"))

# # How would you check if the string y is entirely composed of printable characters?


y.isprintable()

# # How would you insert the string "and" between the strings x and y?


str_1=x+" "+"and"+" "+y
str_1

# # How would you split the string z at each occurrence of the word "Machine"?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
strg=z.split("Machine")
strg

# # How would you replace all spaces in the string x with underscores?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"


strg = x.replace(" ", "_")

print(strg)

# # How would you strip all digits from the string y?


y.strip()

# # How would you check if the string x is a valid identifier?


str1=x
str1
for i in range(len(str1)):
    if ((str1[0]) >= 'a' and str1[0]) <= 'z') or (str1[0]) >= 'A' and str1[0] <= Z') or str1[0] == '_'):
        return False
else:
    return True

# # How would you right-justify the string y in a string of length 10 with "%" as the padding character?


x = "Data Science"
y = "Edukron"
z = "Machine Learning"
count=0
y.rjust(10,"%")

# # How would you swap the case of the string z?


z.swapcase()

# # How would you check if the string x is entirely composed of numeric characters?


x.isnumeric()

# # How would you partition the string y at the first occurrence of the letter "o"?


y.partition('o')

# # How would you convert the string z to title case?


z.title()

# # How would you translate the string y using a translation table that replaces "r" with "R"?


y
mytable = y.maketrans("r", "R")
print(y.translate(mytable))

# # How would you center the string y in a string of length 30 with "_" as the padding character?


y.center(30,"-")

# # How would you remove all occurrences of the word "Data" from the string x?


for i in x:
    if i not in "Data":
        print(i)



