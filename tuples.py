#tuples are immutable
t =  (1,2,3,4,5)
print(t[3])
try:
    t[3] = 10
except:
    print("tuples are immutable")
(x,y)=(10,"python")
print(x)
print(y)
print((2,5,7)>(2,7,3))

c = {'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
