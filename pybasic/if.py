
#If statement:
# a = 30
# b = 40
# if b>a:
#     print("b is greater than a")

# elIf statement:
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# a = 30
# b = 30
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")

# else statement:
# a = 200
# b = 33
# if b>a:
#     print("b is greater then a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater then b")

#short line if statement:
# a = 100
# b = 50
# if a>b: print("a is greater then b")

#One line if else statement:
# a = 20
# b = 30
# print("a") if a>b else print("b")

# And statement:
# a = 100
# b = 30 
# c = 200
# if a > b and c > a:
#     print("Both condition are ture")

# Not statement:
a = 20
b = 50
if not a>b:
    print("a is not greater then b")

#Nested If Statement:
x = 17
if x > 10:
    print(" The number of x above 10")
    if x > 20:
        print("The number of x also above 20")
    else:
        print("But not above 45.")
