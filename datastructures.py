#Datastructures
#create an empty list]
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#find freq of 8 (count)
#find he mean of the list
#find median
#remove duplicates from list and give output in the format of tuple

x = []
y = [5,6,7,8]
z = x + y
print(z)
w = x + [5,6,7,8]
print (w)
q = z + [8,9,1,5,6,7,8,1]
print (q)
r = q.count(8)
print (r)
l = sum(q)
n = len(q)
mean = l/n
print (mean)
median = n/2
print(median)
print(tuple(set(q)))
#=====================================================================================
#Task2
#create 2 empty sets
#
#Task2: Sets

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

a = set()
b = set()
c = {7,8,1,2,3,4,5}
d = {4,5,6,0}
a.update(c)
print(a)
b.update(d)
print(b)
print(b.issubset(a))
print (bool(b.intersection(a)))
a.remove(8)
print(a)
a.discard(0)
print(a)
b.discard(0)
print(b)
u = a.union(b)
print (u)
#===================================================================
#Tuple
##Task3: Tuple

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times
a = (1,4,5,6,7,8)
b = (5,6,7,8,9)
#common elements between 2 tuples
c = set(a)
d = set(b)
print(tuple(d.intersection(c)))
e = a + b
print(e)
f = tuple(set(e))
print (f)
print(f.index(9))
print(3 * f)
#====================================================================
#Dictionary


#Task4: Dictionary:

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

a = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(a[3][0][::2])
c = a[3][2][:-6:-1]
print(c)
print(tuple(a.keys()))
b = a[2]
avg = sum(b)/len(b)
print(avg)
#=================================================================================







