person = {"name":"Punit","age":21}
print(person["age"])
print(person.get("name"))
print(person.get("hobbies"))#prints none
print(person.get("hobbies","dancing"))#prints a default value if key not present
person["name"]="madhav"
print(person.get("name"))
#if you try to assign a value to a key the doesn't exist it adds new key value pair to the dictionary
print(person)
person["house"]="bunglaw"
print(person)
#to remove a key value pair use dictionary.pop(key)//it returns the  value 
print(person.pop("house"))
print(person)
#print(person.pop()) //zero arguments throws error
#iterating through dictionary is possible with for loop //each iteration accessess a single key and we can access the values with the key 
person["house"]="bunglaw"
for key in person:
    print(key+":",person[key]," ")
#COUNTING word occurences
list_of_words = ["hi","hello","wow", "hi","wow","hi"]
count = dict()
# for word in list_of_words:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
##another way of counting
for word in list_of_words:
    count[word] = count.get(word,0)+1
print(count)
list_of_keys = count.keys()#returns the list of keys present in the dictionary as dict_keys()
print(list_of_keys)
#print(count.keys())
print(list(count))#return the an absolute list of keys in the dictionary
print(count.values())
print(count.items()) #returns a list of tuples of the dictionary
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
print(data["calories"])
for i,j in count.items():
    print(i,j)

name=input("Enter the file name:")
try:
    file = open(name)
except IOError:
    print("file not found with the specified name")
else:
    count_dict = dict()
    for line in file:
        words = line.split()
        for word in words:
            count_dict[word] = count_dict.get(word,0)+1

    big_word = None
    big_count = None
    for word,count in count_dict.items():
        if big_count is None or count>big_count:
            big_count = count
            big_word = word
    print("BIg word:",big_word,"count:",big_count)
