try:
    a = int(input("enter numerator:"))
    b = int(input("enter denominator:"))
    c = a/b
    print("the result is",c)
    list = [1,2,3,]
    d = int(input("enter the index:"))
    print("the index value is",list[d])
except ZeroDivisionError:
    print("Division by zero is not possible")
except IndexError:
    print("Index can't be more than than the size of the list")
except IndentationError:
    print("Indentation error is occured")#this program execute but can't handle any indentation errors since program is terminated at the error
finally:
    print("finally block executed")
print("program ends")
