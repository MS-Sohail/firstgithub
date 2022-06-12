# CHAPTER 08 - TYPE CONVERSION

x = 10          # integer
y = 10.5        # float
z = "Hello"     # string

print(x, y, z)

# implicit type conversion
x = x*y
print(x, type(x))
print(y, type(y))

# explicit type coversion

age = input("What is your age? ")
age = int(age)
print(type(age))

# name

name = input("What is your name? ")
print(type(name))