###########accessing elem in tuple

# mytuple1=("apple", "orange", "cherry", "banana")

# print(mytuple1[0])
# print(mytuple1[1])
# print(mytuple1[::-1])
# print(mytuple1[-1])


# for var in mytuple1:
#     print(var)
#
# for var in mytuple1[::-1]:
#     print(var)

###########accessing elem in tuple
#
# tuple1=("apple", "orange", "cherry", "banana")
# # tuple1[0]="grape"#TypeError: 'tuple' object does not support item assignment
# # indirect way
# list1=list(tuple1)
# print(list1)
# list1.append("kiwi")
# print(list1)
# tuple1=tuple(list1)
# print(tuple1)

###############exsistence of ele
# tuple1=("apple", "orange", "cherry", "banana")
# print("apple" in tuple1)#T
# print("apple" not in tuple1)# F
# print(len(tuple1))

#####################3del statement

# tuple1=("apple", "orange", "cherry", "banana")
# # del tuple1[0]#TypeError: 'tuple' object doesn't support item deletion
# del tuple1#NameError: name 'tuple1' is not defined. Did you mean: 'tuple'?
# print(tuple1)

###########
# tuple1=("apple", "orange", "cherry", "banana", "orange", "cherry", "orange", "cherry")
# print(tuple1.count("cherry"))
# print(tuple1.index("cherry",4,6))

########comparator

# tup1=(1,2,3,4,5)
# tup2=(1,2,3,4,5)
#
# print(tup2==tup1)
# print(tup2!=tup1)

########combine
# tup1=(1,2,3,4,5)
# tup2=(1,2,3,4,5)
#
# print(tup2+tup1)
# print(tup2)
# print(tup1)

##################copy mech

tup1=(1,2,3,4,5)
tup2=tup1
print(f"tup1 {tup1} id {id(tup1)}")
print(f"tup2 {tup2} id {id(tup2)}")



tup1=(1,2,3,4,5)
tup2=tuple(tup1)
print(f"tup1 {tup1} id {id(tup1)}")
print(f"tup2 {tup2} id {id(tup2)}")
