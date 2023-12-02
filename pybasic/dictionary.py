
# product_name = {"brand": "hp",        # Shobgolo ke print korte chaile
#                 "model": "m1",
#                 "price": "40000",
#                 "year": "1997"}
# print(product_name)

# product_name = {"brand": "hp",        # Kono akti ke print korte chaile 
#                 "model": "m1",
#                 "price": "40000",
#                 "year": "1997"}
# print(product_name["brand"])

# product_name = {"brand": "hp",        # Onek gola year takle last r ta print hobe
#                 "model": "m1",
#                 "price": "40000",
#                 "year": 1997,
#                 "year": 1952,
#                 "year": 1922}
# print(product_name)

# product_name = {"brand": "hp",      #to find len of the variable
#                 "model": "m1",
#                 "price": "40000",
#                 "year": "1997",
#                 "year1": "1952"
#                 }
# print(len(product_name))

# product_name = {"brand": "hp",          # String, int, boolean, and list data types:
#                 "model": False,
#                 "price": 40000,
#                 "colors": ["red", "white", "green", "blue"]}
# print(product_name)

# product_name = {"brand": "hp",        # Print the data type of a dictionary
#                 "model": "m1",
#                 "price": "40000",
#                 "year": "1997"}
# print(type(product_name))

# product_name = dict(name = "abdullah", age = 28, country = "bangladesh")    # Using the dict() method to make a dictionary:
# print(product_name)


# it's name accessing item:
# product_name = {"brand": "hp",      # Get the value of the "model" key
#                 "model": "m1",
#                 "price": "40000"}
# x = (product_name["model"])
# print(x)

# product_name = {"brand": "hp",      # Get the value of the key's
#                 "model": "m1",
#                 "price": "40000"}
# x = product_name.keys()
# print(x)

# car = {"brand": "hp",
#        "model": "m1",
#         "year": "1997"}
# x = car.keys()
# print(x)
# car["color"] = "white"
# print(x)

#to get values
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# x = product_name.values()
# print(x)

# to get items:
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# x = product_name.items()
# print(x)

# #Check if Key Exists
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# if "model" in product_name:
#     print("yes,'model' is one of the keys in the product_name dictionary")

# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# product_name.update({"price":2000})
# print(product_name)

#The pop() method removes the item with the specified key or values name:
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# product_name.pop("model")
# print(product_name)

# Print all key names in the dictionary, one by one:
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# for x in product_name:
#     print(x)

#Print all values in the dictionary, one by one:
# product_name = {"brand": "hp",      
#                "model": "m1",
#                "price": "40000"}
# for x in product_name:
#     print(product_name[x])

#Loop through both keys and values, by using the items() method:
product_name = {"brand": "hp",      
               "model": "m1",
               "price": "40000"}
for x,y in product_name.items():
    print(x,y)

# my_family = {"child1":
#                 {"name":"rakib",
#                 "age": "20",
#                 "year":"2000"}
#             "child2":
#                 {"name": "mohit",
#                 "age": "22",
#                 "year": "2002"}
#             {"child3":
#                 "name": "rana",
#                 "age": "23",
#                 "year": "2003"}}
# print(my_family)


