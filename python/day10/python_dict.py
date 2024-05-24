#unordered
#muatable
# collection key - value
# key unique

#######create

# d1={1:"one", 2:"two", 3:"three",4:[1,2,3,4]}
# print(d1)
################empty dict

# d2={}
# d3=dict()

###############
# d1={1:"one", 2:"two", 3:"three",4:[1,2,3,4], 1:"first", 1:"abcdef"}
# print(d1)

# d1={"brand":"Maruthi", "year": "2023", "model":1102, "brand":"hyndai"}
# print(d1["brand"])
# print(d1["year"])
# print(d1["model"])
#
# print(d1.get("brand"))
# print(d1.get("year"))
# print(d1.get("model"))


################### add and update
# d1={"brand":"Maruthi", "year": "2023", "model":1102}
###appr1
# d1["color"]="black"
# print(d1)
# d1["year"]="2024"
# print(d1)

###appr2

# d1.update({"color":"red", "seats":4})
# print(d1)#{'brand': 'Maruthi', 'year': '2023', 'model': 1102, 'color': 'red', 'seats': 4}
# d1.update({"year":"2024", "seats":7})
# print(d1)

################using for loop
# d1={'brand': 'Maruthi', 'year': '2023', 'model': 1102, 'color': 'red', 'seats': 4}

# for var1, var2 in d1:
#     print(var1, var2)#ValueError: too many values to unpack (expected 2)

# print(d1.values())#dict_values(['Maruthi', '2023', 1102, 'red', 4])
# print(d1.keys())#dict_keys(['brand', 'year', 'model', 'color', 'seats'])
# print(d1.items())#dict_items([('brand', 'Maruthi'), ('year', '2023'), ('model', 1102), ('color', 'red'), ('seats', 4)])

# for k in d1.keys():
#     print(k)
#
#
# for v in d1.values():
#     print(v)
#
# for k,v in d1.items():
#     print(f"key:{k} val:{v}")


#########check exsistence of key and value

# d1={'brand': 'Maruthi', 'year': '2023', 'model': 1102, 'color': 'red', 'seats': 4}

# print("model" in d1.keys())
# print("model" not in d1.keys())
# print("2023" in d1.values())
# print("2023" not in d1.values())

# print(len(d1))

#########################3remove

# d1={'brand': 'Maruthi', 'year': '2023', 'color': 'red', 'seats': 4, 'model': 1102}

# app1
# d1.pop("model")
# print(d1)

#appr2
# d1.popitem()
# print(d1)

##appr3
# del d1["brand"]
# print(d1)

# del d1
# print(d1)#NameError: name 'd1' is not defined

# appr4
# d1.clear()
# print(d1)

###############combine

# d1={'brand': 'Maruthi', 'year': '2023'}
# d2={'color': 'red', 'seats': 4, 'model': 1102}
# d1.update(d2)
# print(d1)
# d2.update(d1)
# print(d2)

# print(d1+d2)#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


#############copy

d1={'brand': 'Maruthi', 'year': '2023'}
# d2=d1# shallow copy
# print(f"d1{d1} id {id(d1)}")
# print(f"d2{d2} id {id(d2)}")
# d1["brand"]="hyndai"
# print(f"d1{d1} id {id(d1)}")
# print(f"d2{d2} id {id(d2)}")


# d2=d1.copy()# deep copy
d2=dict(d1)# deep copy
print(f"d1{d1} id {id(d1)}")
print(f"d2{d2} id {id(d2)}")
d1["brand"]="hyndai"
print(f"d1{d1} id {id(d1)}")
print(f"d2{d2} id {id(d2)}")