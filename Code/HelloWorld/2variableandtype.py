# coding=utf-8
myint = 7
print('int value :' + str(myint))

myfloat = 7.1
print("float value :" + str(myfloat))

print('int to float value : ' + str(float(myint)))
# number 数据类型 integer float两种

one = 1
two = 2
print(one + two)

hello = "hello "
world = "world"
print(hello + world)

mystring1 = 'string defined with single quote...'
print(mystring1)

mystring2 = "string defined with double quote."
print(mystring2)

# string  单引号 和 双引号两种定义方式

print("print does't")

print('"yes",he said.')

print('"isn\'t it",he said.')

s = 'first line \n second line.'
print(s)

mystring = "Don't worry about apostrophes"
print(mystring)

a, b = 3, 4
print(a, b)

mystring = "hello world"
myfloat = 10.0
myint = 20

# testing code

if mystring == 'hello world':
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("float:%f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("integer : %d " % myint)
