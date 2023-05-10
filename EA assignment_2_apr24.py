# -*- coding: utf-8 -*-

# -- Sheet --

list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 

x="data science"
y="machine learning"
z="edukron"

# # Write a Python program that takes the given list and creates a new list containing only the items that are longer than 12 characters.


lst=[]
list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
for i in list_example1:
    x=len(i)
    #print(x)
    if len(i)>=12:
        #print("the word:{0} has length: {1}".format(i,x))
        lst.append(i)
print(lst)

       

# # Write a Python program that takes the given list and creates a new list containing only the items that contain the letter "a".


lst=[]
list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
for i in list_example1:
    if 'a' in i:
        print(" the words which has letter :a are: {0}".format(i))
        lst.append(i)
    #print(i.find('a'))
print(lst)

               

# # Write a Python program that takes the given list and creates a new list where each item is capitalized.


lst=[]
list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
for i in list_example1:
    x=i.capitalize()
    print(x)
    lst.append(x)
print(lst)

# # Write a Python program that takes the given list and creates a new list where each item is reversed.


lst=[]
list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
# list_example1.reverse()
# print(list_example1)

list_example1[::-1]


# # Write a Python program that takes the given list and creates a new list where each item is sorted in reverse alphabetical order.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
list_example1.sort()
print(list_example1)


# # Write a Python program that takes the given list and creates a new list where each item is sorted by the number of vowels it contains.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
count=0
for i in range(len(list_example1)):
    print(len(i))


# print(vowelCounter(["terrapin","station","13points"]))


# string="data structure"
# vowels=['a','e','i','o','u']
# count=0
# for i in string:
#     if i in vowels:
#         count=count+1
#         print(i)
# print(count)



# # Write a Python program that takes the given list and creates a new list where each item is a tuple containing the original item and its length.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]


# new_list=[(i, len(i)) for i in list_example1]
# print(new_list)


for i in list_example1:
    print([(i, len(i))])

# # Write a Python program that takes the given list and creates a new list where each item is a dictionary containing the original item as the key and its length as the value.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]


# new_list=[(i, len(i)) for i in list_example1]
# print(new_list)

# y=[]
# for i in list_example1:
#     x=i
#     y.append(len(i))

# d1=zip(list_example1,y)

# print (dict(d1))


for i in list_example1:
    print([dict(i, len(i))])







# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with " - AI" added to the end.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
new_lst=[]
for i in range(len(list_example1)):
    new_lst.append(list_example1[i] + 'AI')
print(new_lst)



# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with the vowels replaced with asterisks.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"]
count=0
vowels=['a','e','i','o','u']
for i in range(len(list_example1)):
    if i in vowels:
        count=count+1
        print(list_example1[i], count)

# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with the first and last letters removed.


test_list=["data science","machine learning","data analytics","edukron","artificial intellgience"]


 

#res = [sub[1:] for sub in test_list]
for sub in test_list:
    res=sub[1:-1]
 
# printing result
    print("The list after removing first and last characters : " + str(res))

# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with every other letter removed.




# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with the words reversed in order (e.g. "data science" becomes "science data").


test_list=["data science","machine learning","data analytics","edukron","artificial intellgience"]


 

#res = [sub[1:] for sub in test_list]
for sub in test_list:
    res=sub[::-1]
 
# printing result
    print("The word: '{0}' after reversing is : " .format(sub) + str(res))

# # Write a Python program that takes the given list and creates a new list where each item is a string containing the original item with the words sorted alphabetically (e.g. "data science" becomes "science data").


test_string=["data science","machine learning","data analytics","edukron","artificial intellgience"]

test=[]
for i in range(len(test_string)):
    x=test_string[0]
print(x)
#test.append(test_string[0])

for i in x:
    print(i)








