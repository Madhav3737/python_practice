def generate_even():
    n=0
    yield n
    n+=2
    yield n
    n+=2 
    yield n
even = generate_even()
print("even numbers")
print(next(even))
print(next(even))
print(next(even))
#print(next(even))#generates error
def fibonacci():
    n1=0
    n2=1
    while True:
        yield n1
        n1,n2 = n2,n1+n2

fibonacci_number = fibonacci()
print("fibonacci Numbers")
for i in range(10):
    print(next(fibonacci_number))
def odd_generate():
    n = 1
    while True:
        yield n
        n+=2
print("odd Numbers")
odd_number=odd_generate()
for i in range(10):
    print(next(odd_number))
    

