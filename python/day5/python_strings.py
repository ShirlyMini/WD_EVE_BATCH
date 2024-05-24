#create string
# str1="python"
# str2='python'
# str3=str("python")
# str4=str('python')
#
# print(str1)
# print(str2)
# print(str3)
# print(str4)
#
# print("I'm strong")
# print('I"m strong')
# print('I"m strong "/path"')

##### empty string

# str1=""
# str2=''
# str3=str()
# print(str1)
# print(str2)
# print(str3)

##### string slicing

# str1="welcome to python" # loc starts from 0 to n-1
# print(str1[0])#using indexing
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[0:7])#([start=0:end=n-1:step=1])welcome
# print(str1[:7])# welcome
# print(str1[:])#welcome to python
# print(str1)#welcome to python
#
# print(str1[3:10])#come to
# print(str1[3:10:2])#cm o

####negative indexing
# str1="welcome to python"
#-17 to -1
# print(str1[-1])#
# print(str1[-2])
# print(str1[-3])
#
# print(str1[-17:-10])#welcome
# print(str1[-17:-10])#welcome
# print(str1[-6:-1])#pytho
# print(str1[-6:0])#prints nothing
# print(str1[-6:])#python

# ####### reverse the string
# str1="welcome to python"
# print(str1[::-1])

##################string with for loop
# str1="welcome to python"
# for var in str1:
#     print(var)

# for var in str1[::-1]:
#     print(var)

# for var in str1[-6:]:
#     print(var)

###############reverse string using for loop

# str1="welcome to python"
# rev_str=""
#
# for var in str1:
#     # print(var)
#     rev_str=var+rev_str
# print(rev_str)

#########################3

# print(list(reversed("welcome to python")))
# # list to str conv
# print("".join(list(reversed("welcome to python"))))
# print("**".join(list(reversed("welcome to python"))))
# print(" ".join(list(reversed("welcome to python"))))
# print(", ".join(list(reversed("welcome to python"))))

###########################len string

# str1="welcome"
# print(len(str1))# count of bytes

#######################in and not in operator
str1="welcome to python"

print("python" in str1)
print("python" not in str1)

print("Python" in str1)
print("Python" not in str1)
