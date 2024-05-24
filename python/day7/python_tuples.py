#order and immuatable
# ()

#######create tuple
# mytuple=(10, "apple", [1,2,3,4], 1.2)
# mytuple=tuple((10, "apple", [1,2,3,4], 1.2))
# print(mytuple)
# print(type(mytuple))

############3empty tuple

# mytup=()
# print(mytup)
# # or
# mytup=tuple()
# print(mytup)

################
str1="string"
list1=[1,2,3,4,5]
tup1=(10,20,30)
print(list(tup1))
print(list(str1))
print(tuple(list1))
print(type(str(list1)))
print(str(list1))
print(str(list1)[0])