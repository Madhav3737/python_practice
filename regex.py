import re
x = "my 2 favourite numbers are 19 and 42"
z =re.search("fav",x)#returns boolean value>>  <re.Match object; span=(5, 8), match='fav'>
print(z)
y = re.findall("[0-9]+",x)
print(y)

email= "iamnot.fake.123@gmail.com"
host = re.findall(".*@([^ ]*)",email)
print(host)

p = re.compile('[0-9]')
print(p.findall(email))
from re import split
print(split('\W+', 'Words, words , Words'))#splitting using a non word character
print(split('\W+', "Word's words Words"))
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))