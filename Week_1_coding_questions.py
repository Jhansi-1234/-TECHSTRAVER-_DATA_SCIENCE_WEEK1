#lists
lis=['a','b','c','d','e']
print(lis)
#creating a list with mixed type of values
lis1=[1,2,3,'john']
print(lis1)
#appending using append()
lis.append('f')
print(lis)
#reversing a list
print("reversed list using in-built functions")
lis.reverse()
print(lis)
list(reversed(lis))
print(lis)
#reversing a list
list2=[]
for i in lis:
  list2.insert(0,i)
print(list2)
#deleting a list
lis.clear()
print(lis)
# dictionaries
from collections import OrderedDict
dict1 = {'name': 'jhan', 'age': 20}
print(dict1)
# After appending using square bracket notation
dict1['salary'] = 100000
print(dict1)
# Appending using update method
dict1.update({'city': 'hyderabad'})
print(dict1)
# Appending using setdefault
dict1.setdefault('Mobile Number', 9563214855)
print(dict1)
#reversing dictionary
rev_dict={}
for key,value in dict1.items():
    rev_dict[value]=key
print(rev_dict)
# deleting a key in dictionary
del dict1['Mobile Number']
print(dict1)
# using pop() in dictionary
p=dict1.pop('city')
print(p)
print(dict1)
# sets
#creating a set in python
set1={1,2,3,4,5}
print(set1)
#appending element to a set
set1.add(6)
print(set1)
#adding an iterable to set
f=[10,11]
t=(7,8,9)
set1.add(t)
set1.update(f)
print(set1)
#removing iterable in python
set1.remove(t)
print(set1)
#reversing a set in python
print("Reversed set")
for _ in range(len(set1)):
  ele=max(set1)
  set1.remove(ele)
  print(ele, end=',' if set1 else '')
#removing a set in python
print("\nremoving set")
set1.clear()
print(set1)
# tuples
#creating a tuple
tup=(1,2,3,4)
print(tup)
#appending 
new_tup=(5)
print("appending tuple")
appended_tuple=tup+(new_tup,)
print(appended_tuple)
#reversing a tuple
print("reversing a tuple")
def reverse(tuples):
  re_tup=tuples[::-1]
  return re_tup
print(reverse(appended_tuple))
#deleting a tuple
del appended_tuple
#clearing the dictionary
dict1.clear()
print(dict1)
#deleting the dictionary
del dict1
