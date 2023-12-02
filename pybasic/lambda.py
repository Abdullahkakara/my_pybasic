
# x = lambda a: a + 10
# print(x(10))

# x = lambda a,b: a * b
# print(x(7,7))

# x = lambda a,b,c:a+b+c
# print(x(7,1,2))

def name(n):
    return lambda a : a * n
mydoubler = name(5)
print(mydoubler(11))


