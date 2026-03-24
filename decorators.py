#In python decorators are functions which other functions as parameter and adds some functoinality to it 
#Everything in python is an object and varibles identifiers bound to these objects 
#since functions are also objects we can pass them as parameters 

#Example for passing a function as a parameter 
def main_func(x):
    return x+1
def operate(func,x):
    result=func(x)
    return result
print(operate(main_func,54))

#we can also define a function inside a function
def print_message(msg):
    greeting = "hello"
    def printer():
        print(greeting,msg)
    printer()
print_message("Python is awesome")

#a function can also return another function
def print_message(msg):
    greeting = "hello"
    def printer():
        print(greeting,msg)

    return printer
func = print_message("Python is awesome")
func()#here the func function holds the greeting and msg variabls even after the outer function is done executing , such a function is called closure

#Now we can learn decorators
def printer():
    print("This is the printer function")
def decorating_function(func):
    def inner():
        print("executing the",func.__name__,"Function")
        func()
        print("done executing the function")
    
    return inner
printer()
decorated_function = decorating_function(printer)
decorated_function()

#instead of cerating a function variable and decotatin it we can use '@' to decorate a function with a previously defined decorator function
@decorating_function
def new_printer():
    print("This is the new printer function")

new_printer()

#In the above discussed example the decorator function did not take any parameters now let us discuss a decorate function with parameters
def smart_division(func):#decorating function
    def inner(a,b):
        print("dividing",a,"by",b)
        if b==0:
            print("Can't divide by Zero")
            return
        return func(a,b)
    return inner

@smart_division
def divide(a,b):
    return a/b

print("a/b=",divide(14,2))
print("a/b=",divide(54,0))
# it is equivalent to 
# decorated division = smart_division(divide)
# decorated_division(14,2)

#A functioon can be decorated multiple times
def star(func):
    def inner(msg):
        print("*"*30)
        func(msg)
        print("*"*30)
    return inner

def hashtag(func):
    def inner(msg):
        print("#"*35)
        func(msg)
        print("#"*35)
    return inner

@hashtag
@star
def print_msg(msg):
    print(msg)

print_msg("the message printing Function")
print_msg("Hello world!")
# it is equivalent to 
# decorated_function = hashtag(star(print_msg))
# decorated_function("Hello world!")






