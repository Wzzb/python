phonebook = {}
phonebook["John"] = 12443
phonebook[2] = 'hello'
phonebook[3.2] = 3.2

print(phonebook)
print(phonebook[3.2])

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Iterating over dictionaries
for name,number in phonebook.items():
    print("Phone number of %s is %d"%(name,number))

#removing a value

del phonebook["John"]
print(phonebook)

phonebook["John"] = 938477566
print(phonebook)

phonebook.pop("Jack")
print(phonebook)

if "Jill" in phonebook:
    print("Jill is in phonebook.")