#reading from a file
f = open("hello.txt","r")
content = f.read()
print(content)
f.seek(0)
lines = f.readlines()
print(lines)
f.close()
try :
    f = open("hello.txt","r")
    content = f.read()
    print(content)
    f.seek(0)
    lines = f.readlines()
    print(lines)
finally:
    f.close()

with open("hello.txt","r") as f:#doesn't require close operation
    f = open("hello.txt","r")
    content = f.read()
    print(content)
    f.seek(0)
    lines = f.readlines()
    print(lines)

##writing in a file 
f = open("python.txt","w")
f.write("hi this is python file \n we going to write in this file")
print('writin in the file successful')
f.flush()
f.close()

with open("python.txt","a") as f:
    f.write("\n this is an appended line")
    f.writelines(["\nhieee","\n hello"])
