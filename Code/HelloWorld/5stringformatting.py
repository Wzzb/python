name = "Jessie"
print("Hello , %s" % name)

age = 23
print("%s is %d years old" % (name, age))

mylist = [1, 2, 3]
print("mylist is " + mylist.__repr__())


data = ("John","Doe",53.44)
format_string = "Hello %s %s, Your current balance is $%s."
print(format_string %data)