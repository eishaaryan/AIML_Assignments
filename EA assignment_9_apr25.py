# -*- coding: utf-8 -*-

# -- Sheet --

x={"data science","machine learning","artificial intelligence"}
y={"data science","ai","machine learning","deep learning"}

# # How would you find the intersection of sets "x" and "y"?


x.intersection(y)
##Intersection takes common words in set

# # How would you find the union of sets "x" and "y"?


x.union(y)
##union takes uncommon words

# # How would you find the difference of sets "x" and "y"?


x.difference(y)

# # How would you find the symmetric difference of sets "x" and "y"?


x.symmetric_difference(y)

# # How would you check if set "x" is a subset of set "y"?


x.issubset(y)

# # How would you check if set "y" is a superset of set "x"?


y.issuperset(x)

# # How would you add the element "deep learning" to set "x"?


x.add("Deep Learning")
x

# # How would you remove the element "ai" from set "y"?


y.remove("ai")
y

# # How would you clear all the elements from set "x"?


x.clear()
x

# # How would you check if the element "data science" is in set "y"?



'data science' in y

# # How would you check if the element "python" is not in set "x"?


'python' not in x

# # How would you create a new set that contains all the elements from set "x" that are not in set "y"?


x.difference(y)

# # How would you create a new set that contains all the elements from set "y" that are not in set "x"?


y.difference(x)

# # How would you loop through all the elements in set "x"?


for i in x:
    print(i)

# # How would you loop through all the elements in set "y"?


for i in y:
    print(i)

# # How would you find the length of set "x"?


len(x)

# # How would you find the length of set "y"?


len(y)

# # How would you create a copy of set "x"?


x.copy()
x

# # How would you create a copy of set "y"?


y.copy()

# # How would you remove all the common elements between set "x" and set "y"?


x.symmetric_difference(y)



