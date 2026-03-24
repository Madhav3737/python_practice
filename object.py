i =1
print(type(i))
print("id of i=",id(i))
print(dir(i))
flag = True
print(type(flag))
def my_function():
    pass
print(type(my_function))
l = [1,2,3,4]
print(type(l))
print(dir(l))
a = 5
b = a
print("id of a=",id(a))
print("id of b=",id(b))
c = [1,2,3,4,5]
print("c = ",c)
d = c
print("d = ",d)
c.append(6)
print("c = ",c)
print("d = ",d)
e = c.copy()
print("c = ",c)
print("e = ",e)
c.append(7)
print("c = ",c)
print("e = ",e)
for i in l:
    print(i)
print(l)
if i==4:
    print("i value sustained")