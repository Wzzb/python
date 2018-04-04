number = 1 + 2 * 3 - 1;
print(number)

number = 3 / 2
print(number)
print(float(number))

number = 3 / 2.0
print(number)

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared + cubed)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers;
print(all_numbers)

print([1,2,3]*3)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list size = %d" % len(x_list))
print("y_list size = %d" % len(y_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

print(big_list)