# CHAPTER 10 - FUNCTIONS

print("I love Aaliyar!")
print("I love Aaliyar!")
print("I love Aaliyar!")

# 1 Defining a function

def aali():
    print("I love Aaliyar!")
    print("I love Aaliyar!")
    print("I love Aaliyar!")

aali()

# 2

def aali():
    text = "We love Aaliyar Ahmed"
    print(text)
    print(text)
    print(text)

aali()

# 3

def aali(text):
    print(text)
    print(text)
    print(text)

aali("We love Aaliyar Ahmed")

# 4 defining a function with if, elif and else statements

def school_calculator(age):
    if age==5:
        print("Aaliyar can join the school.")
    elif age>5:
        print("Aaliyar should join college")
    else:
        print("Aaliyar is still a baby.")

school_calculator(5)

# future function

def future_age(age):
    new_age = age+20
    return new_age
    print(new_age)

predicted_age = future_age(18)
print(predicted_age)

