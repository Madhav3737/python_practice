numbers = [1,2,3,4,5]
value = numbers.__iter__()
print (value.__next__())
print (value.__next__())
print (value.__next__())
print (value.__next__())
print (value.__next__())
print("\n")
value2 = numbers.__iter__()
print (next(value2))
print (next(value2))
print (next(value2))
print (next(value2))
print (next(value2))
print("\n")
value3 = iter(numbers)
print (next(value3))
print (next(value3))
print (next(value3))
print (next(value3))
print (next(value3))
#print (next(value3))
print("\n")

value4 = iter(numbers)
while(True):
    try:
        print(next(value4))
    except StopIteration:
        break

print("Even numbers with Iterators")
class Even:
    def __init__(self,max):
        self.n = 2
        self.max = max
    def __iter__(self):
        return self#what is the use
    def __next__(self):
        if self.n<=self.max:
            result = self.n
            self.n+=2
            return result
        else:
            raise IndexError

even = Even(10)
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())
#print(even.__next__())



