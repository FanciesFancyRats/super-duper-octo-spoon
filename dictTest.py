dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
list1 = list()
print dict1
for key, value in dict1.items():
    print key, "key has the value", value
string1 = "abcd"
for i in range(len(string1)):
    print string1[i] in dict1.items()
    print dict1.items()
for key, value in dict1.items():
    list1.append(key)
    list1.append(value)
print list1
print 
