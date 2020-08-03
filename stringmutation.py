string = "abracadabra"
l = list(string)
print(l)
l[5] = 'k'
string = "".join(l)
print (string)
#Another way of modifying element value in string.
string = string[:5] + "a" + string[6:]
print(string)
