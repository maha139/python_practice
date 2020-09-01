
#program 1. Get two values (input) ===> number, string

#7 , "python" ===> pythonpythonpythonpythonpythonpythonpython777777

#3 , "perl"   ===> perlperlperl3333

val_a = input("Enter the number: ")
val_b = input("Enter the string: ")
u = val_b * int(val_a)
print(u)
v = len(val_b) * val_a
w = u + v
print(w)



#program 2. Get two values (input) ===> string, number

#computer_science, 3 ===> mocputer_scieecn

#biology , 2  ===> iboloyg

# Reverse the string from the position before that

val_a = input("Enter the number: ")
val_b = input("Enter the string: ")
a = int(val_a)
b = val_b[:a] #extract com from var
c = val_b[-a:] #-1 -2 -3 back he has taken
print(b)
print(c)
b_reverse = b[::-1]
c_reverse = c[::-1]
x = val_b[a:-a]
print(x)
print(b_reverse+x+c_reverse)


#Capital program string
#program 3:

#get two strings from user  computer science  ==> input 

#step 1 ==> comPuter  sciEnce

#step 2 ===> concatenate both ==> comPutersciEnce

#step 3 ===> comPuteRsciEnce
val_a = input("enter the first string:")
val_b = input("enter the second string:")
c = len(val_a)
d = len(val_b)
e = int(c/2)
f = int(d/2)
a1 = (val_a[e])
b1 = (val_b[f])
a = a1.upper()
b = b1.upper()
print(a1)
print(b1)
a = val_a.replace(a1,a2,1)
b = val_b.replace(b1,b2,1)
print(a)
print(b)
x = a + b
print(x)
y = int(len(x)/2)
y1 = int(y)
y2=x[y1]
y3 = y2.upper()
z = y.replace(y2,y3)
print(z)
############################################
LIST OF NUMBERS
##########################################
#Task 1 ===> first ele + middle ele + last ele /3
#Task 2 ===> one number ===> index ==> index
#index ==3 ===> [2,3,4,5,100,101,102,103,104,1]
#program 4:

#[103,104,1,2,3,4,5,100,101,102]  ==> hard coded 

#Task 1 ===> first ele + middle ele + last ele  / 3

#Task 2 ===> one number ===> index  ==> index

#index ==3  ===> [2,3,4,5,100,101,102, 103,104,1]
a = [103,104,1,2,3,4,5,100,101,102]
b = (a[0] + a[-1] + a[len(a)/2]) / 3
print(b)

i = int(input("enter the element to find corres index:"))
c = a.index(i)
print(c)
d = int(input("Enter the index: "))
a = a[d:] + a[:d]
print(a)

============================
#Program 5:

#{1: 100, 2:101, 3: 103, 4:104, 5:105}

#Task1 ===> sum all values / sum of all keys 

#Task2 ===> Max(values) / Min(key)
#Sum of all values / sum of all keys

a = { 1:100, 2:101, 3:103, 4:104, 5:105}
v = sum(a.values())
k = sum(a.keys())
print(k)
print(v)
avg = v/k
print(avg)
print(k)
x = max(a.values())
y = min(a.keys())
z = x / y
print(z)













