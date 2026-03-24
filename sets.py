#sets are same asthe sets in the mathematics
#items of a set are not in any particular order
#No duplicate items are allowed 
#Items must be immutable objects
#sets are mutable in python
animals={"dog","cat","tiger","elephant"}
print(animals)#{'dog', 'cat', 'elephant', 'tiger'}

animals={"dog","cat","tiger","elephant","dog","elephant"}
print(animals)#{'tiger', 'cat', 'elephant', 'dog'}//deletes the duplicate elements

animals1 =set()#creates an empty set
print(animals1)#set()

list=["snake","cheetah","buffalo"]
animals2=set(list)#OR animals2=set(["snake","cheetah","buffalo"])
print(animals2)#{'cheetah', 'snake', 'buffalo'}

animals.add("monkey")#adds an element to the set
print(animals)

animals.update(list)#Adds a list of elements to the set
print(animals)

animals.update(list,{"whale","dolphin"})#we can add multiple iterables to the set using update function
print(animals)

animals.discard("cat")#removes an item from the set and returns none if item not found
animals.remove("dog")#same as the discard function and throws an error if item not found

#union operation
animals_park = animals.union(animals2)#using union function
animals_park = animals | animals2 #using pipe(|) operator
print(animals_park)

#intersection operator
animals3 = animals.intersection(animals2)#using intersection function
animals3 = animals & animals2#using aperes and(&) operator
print(animals3)



