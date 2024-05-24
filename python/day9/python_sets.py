# set1={"apple", "orange", "cherry", "banana"}
# set2={"apple", "orange", "cherry", "banana","apple", "apple", "apple"}
# duplicates aare not allowed

###########len
# print(len(set1))
# print(len(set2))

#####removing duplicates
# lst1=["apple", "orange", "cherry", "banana","apple", "apple", "apple"]
# set1=set(lst1)
# print(list(set1))

#############exsistence of elem
# set1={"apple", "orange", "cherry", "banana"}
# print("apple" in set1)#T
# print("apple" not in set1)#f


###################3remove elem
# set1={"apple", "orange", "cherry", "banana"}
# appr1
#
# set1.pop()
# print(set1)

#appr2
# set1.remove("orange")
# print(set1)

# set1.discard("orange")
# print(set1)
#####with non exsisting elem
# set1.remove("1234")
# print(set1)#KeyError: '1234'

# set1.discard("1234")
# print(set1)

###########################copy
# set1={1,2,3,4,5,6}
# # set2=set1# shallow copy
# # set2=set1.copy()# deep copy
# set2=set(set1)# deep copy
# print(f"set1 {set1} and id {id(set1)}")
# print(f"set2 {set2} and id {id(set2)}")
# set1.pop()
# print(f"set1 {set1} and id {id(set1)}")
# print(f"set2 {set2} and id {id(set2)}")

#######################set properties

# set1={1,2,3,4,5,6,10,20}
# set2={1,2,10,20,30,40,50,60}
# # set3={7,8,9}
#
# # print(set1+set2)#TypeError: unsupported operand type(s) for +: 'set' and 'set'
# # print(set1.union(set2))###combine
# var = set1.intersection(set2)###returns common values
# print(var)
# print(set1)
# var=set1.intersection_update(set2)###returns common values
# print(var)
# print(set1)
# print(set1)
# print(set1.difference(set2))### to retive unique values#{3, 4, 5, 6}
# print(set2.difference(set1))
# print(set2.difference_update(set1))
# print(set2)
# print(set1.isdisjoint(set2))#### return true if no common value
# print(set1.isdisjoint(set3))

# print(set1.symmetric_difference(set2))#{3, 4, 5, 6, 40, 50, 60, 30}

###########frozen set

set1={1,2,3,4,5,6,10,20}
set2={1,2,10,20,30,40,50,60}

print(set1)
print(set2)
# var=set1.intersection(set2)
# print(var)
# print(set1.intersection(set2))
# print(set1.difference(set2))

print(set1.intersection_update(set2))
print(set1)
# print(set1.difference_update(set2))
# print(set1)
print(set2.difference_update(set1))
print(set2)