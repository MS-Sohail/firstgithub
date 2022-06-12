# CHAPTER 11 - LOOPS
# while and for loops

# while loop

x = 0
while x<5:
    print(x)
    x = x+1

# for loop

for x in range(5,10):
    print(x)

# Arrays

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    if d=="Fri":
        break
    if d=="Fri":
        continue
    print(d)

