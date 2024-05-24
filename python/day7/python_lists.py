#[]
# ordered and mutable
#######create list
# mylist1=[10, "apple", [1,2,3,4], 1.2]
# mylist1=list([10, "apple", [1,2,3,4], 1.2])
# print(mylist1)
# print(type(mylist1))

############3empty list

# mylist1=[]
# print(mylist1)
# # or
# mylist1=list()
# print(mylist1)

###############accessing elem
#
# mylist=["apple", "orange", "cherry", "banana"]
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[1:3])
# print(mylist[-1])

###################for loop

# for var in mylist:
#     print(var)

# for var in mylist[::-1]:
#     print(var)

###################changing exsisting elem


# mylist=["apple", "orange", "cherry", "banana"]
# mylist[1]="grape"
# print(mylist)

#######################length

# mylist=["apple", "orange", "cherry", "banana", "kiwi"]
# print(len(mylist))
#
# ###############exsistence of an elem
#
# print("kiwi" in mylist)
# print("kiwidcdscdsa" in mylist)
#
# print("kiwi" not in mylist) # F
# print("kiwidcdscdsa" not in mylist) #T

######################Add

# mylist=["apple", "orange", "cherry", "banana"]
# # appr1
# # mylist.append("grape")
# # mylist.append("kiwi")
# # print(mylist)
#
# # appr2
# mylist.insert(2, "grape")
# print(mylist)

##############################33Remove

# mylist=["apple", "orange", "cherry", "banana", "kiwi", "grape"]

#appr1

# mylist.pop()
# print(mylist)
# mylist.pop(1)
# print(mylist)

# appr2

# mylist.remove("cherry")
# print(mylist)

#appr 3
# del mylist[3]
# print(mylist)
#
# del mylist
# print(mylist)#NameError: name 'mylist' is not defined. Did you mean: 'list'?

# appr4
# mylist.clear()
# print(mylist)


###############################combine two list

# list1=[10,20, 30, 40, 50]
# list2=["apple", "orange", "cherry"]

# appr 1
# print(list1+list2)

# appr2
# list2.extend(list1)
# print(list1)
# print(list2)

# appr3

# for i in list2:
#     print(i)
#     list1.append(i)
# print(list1)

########################comapartor


# list1=[10,20, 30, 40, 50]
# list2=["apple", "orange", "cherry"]
#
# print(list2==list1)#F
# print(list2!=list1)#T
# print(list2>list1)TypeError: '>' not supported between instances of 'str' and 'int'


#############################copy

# list1=[1,2,3,4,5,6]
# list2=list1# shallow copy
# print(f"list1 {list1} and ID {id(list1)}")
# print(f"list2 {list2} and ID {id(list2)}")
# list1.remove(6)
# print(f"list1 {list1} and ID {id(list1)}")
# print(f"list2 {list2} and ID {id(list2)}")



# list1=[1,2,3,4,5,6]
# # list2=list(list1)#deep copy
# list2=list1.copy()
# print(f"list1 {list1} and ID {id(list1)}")
# print(f"list2 {list2} and ID {id(list2)}")
# list1.remove(6)
# print(f"list1 {list1} and ID {id(list1)}")
# print(f"list2 {list2} and ID {id(list2)}")

#  mutable
#
# l1=[1,2,3]
# print(f"l1 {l1} and ID {id(l1)}")
# l1.append(4)
# print(f"l1 {l1} and ID {id(l1)}")


##########################

# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print(l1.append(l2))
# print(l1)

