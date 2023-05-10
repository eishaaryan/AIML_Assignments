# -*- coding: utf-8 -*-

# -- Sheet --

list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 

x="data science"
y="machine learning"
z="edukron"

# # Write a Python program that prints the second item in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 

list_example1[1]

# # Write a Python program that adds the item "deep learning" to the end of the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 

list_example1.append("deep learning")
list_example1

# # Write a Python program that removes the item "edukron" from the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
list_example1.remove("edukron")
list_example1

# # Write a Python program that checks whether the item "data science" is in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
for items in list_example1:
    if items=="data science":
        print(True)
        break
    else:
        print(False)
    

# # Write a Python program that prints the length of the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
print(len(list_example1))

# # Write a Python program that sorts the list in alphabetical order.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
list_example1.sort()
list_example1

# # Write a Python program that joins all the items in the list into a single string, separated by commas.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
str1=", ".join(list_example1)
print(str1)

# # Write a Python program that removes the first item in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
del list_example1[0]
list_example1

# # Write a Python program that inserts the item "computer vision" at index 2 in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
list_example1.insert(2,"computer vision")
list_example1

# # Write a Python program that counts how many times the item "machine learning" appears in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
list_example1.count("machine learning")

# # Write a Python program that reverses the order of the items in the list.


list_example1=["data science","machine learning","data analytics","edukron","artificial intellgience"] 
list_example1.reverse()
list_example1

# # Write a Python program that creates a new list containing the items in the original list, but with all the vowels removed.



result=""
list = ["data science","machine learning","data analytics","edukron","artificial intellgience"] 
str1=" ".join(list)
#print(str1)
vowels = ('a', 'e', 'i', 'o', 'u')
for x in str1:
    #print(x)
    if x not in vowels:
        result=result+x
#print(result.split(","))
li = result.split()
print(li)

# # Write a Python program that prints the last three items in the list.


list = ["data science","machine learning","data analytics","edukron","artificial intellgience"]
list[-3:]

# # Write a Python program that prints the first two items and the last two items in the list.


list = ["data science","machine learning","data analytics","edukron","artificial intellgience"]
list[:2]+list[-2:]





