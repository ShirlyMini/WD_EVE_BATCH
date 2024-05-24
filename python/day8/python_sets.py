# unordered
# mutable

# set1={12,"string", 1.2}
# set1=set([12,"string", 1.2])
# set1=set((12,"string", 1.2))
# set1=set({12,"string", 1.2})
# print(type(set1))
# print(set1)

######empty set

# set1={}# dict
# print(set1)
# print(type(set1))# dict
# # or
# set1=set()
# print(set1)
# print(type(set1))


#############3accessing elem

# set1={"apple", "orange", "cherry", "banana"}
# print(set1)
# # print(set1[0])#TypeError: 'set' object is not subscriptable
# for var in set1:
#     print(var)

########add
set1={"apple", "orange", "cherry", "banana"}

# set1.add("kiwi")# add single item
# print(set1)

# set1.update("kiwi")
set1.update({"kiwi","frt1", "frt2"})
print(set1)