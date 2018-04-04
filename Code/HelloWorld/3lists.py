mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)


mylist = [3,4,2,4.5]
mylist1 = ['hello',2]
mylist2 = mylist + mylist1
print(mylist2)

for x in mylist2:
    print(x)

numbers = []
strings = []
names = ["John","Eric","Jessica"]


# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("second name in names list is %s"%second_name)