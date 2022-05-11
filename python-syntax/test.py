# age = 20
# isBirthday = True

# if age >=21:
#     print("you can drink")
#     if isBirthday:
#         print("happy bday, here is a beer")
# elif age>=18:
#     print("you can come in, no drinking")
#     if isBirthday:
#         print("have some juce")
# else:
#     print("go home")


# num = 0
# while num <=100:
#     print(num)
#     num = num + 10
# print("done")


# target = 37
# guess = None

# while guess!= target:
#     guess = input("Please enter a guess...")
#     if guess.startswith("a",0,1) or  guess.startswith("A",0,1):
#         break
#     guess = int(guess)

# print("DONE")

# colors = ["red","orange","yellow","green"]

# for color in colors:
#     print(color)


# for char in "ABCDEFGHIJKL":
#     print(char)

# for n in range(10):
#     print(n)

def greet(person):
    return f"Hello {person}"

def print_upper_words(a):
    for item in a:
        if (item.startswith("e",0,1)) or (item.startswith("E",0,1)): print(item.upper())  

def print_upper_words_v2(a,b):
    for item in a:
        if (item.startswith(b,0,1)) or (item.startswith(b.upper(),0,1)): print(item.upper())






