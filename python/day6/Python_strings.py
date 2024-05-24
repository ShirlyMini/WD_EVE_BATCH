# str1="string"
# print(str1[3])
# # str1[3]="o"#TypeError: 'str' object does not support item assignment
#
# print(id(str1))#140706233348568
# print(id(str1+"sskmksaa"))#2059560612592---immutable


####################### string comparator
#
# print("tim" == "tom")# F
# print("tim" != "tom")# T
# print("tim" > "tom")# F
# print("tim" < "tom")#T

######################3Testing Strings

# str1="welcome"
# str2="1234567"
# str3="string123"
#
# print(str1.isalpha())
# print(str2.isalpha())
# print(str3.isalpha())

# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())

# str4="     "
# print(str1.isspace())
# print(str2.isspace())
# print(str3.isspace())
# print(str4.isspace())

# print(str1.isdigit())
# print(str2.isdigit())
# print(str3.isdigit())
#
# print(str1.isnumeric())
# print(str2.isnumeric())
# print(str3.isnumeric())

# str5="STRING"
# str6="Welcome To Python"
# print(str5.isupper())
# print(str1.islower())
# print(str6.istitle())
# str7="U"
# print(str7.isdecimal())
# print(str7.isdigit())
# print(str7.isnumeric())

####################Finding substring

# str1="welcome to python"

# print(str1.startswith("wel"))
# print(str1.startswith("come"))
#
# print(str1.endswith("on"))
# print(str1.endswith("to"))

# print(str1.startswith("wel", 3,10))
# print(str1.startswith("come", 3,10))
#
# print(str1.endswith("on",3,10))
# print(str1.endswith("on",3))
# print(str1.endswith("to",3,10))
#
# print(str1.find("python"))#11
# print(str1.index("python"))#11
#
# print(str1.find("abc"))#-1
# print(str1.index("abc"))#ValueError: substring not found


# str1="welcome to python to python to python"
# print(str1.count("o"))
# print(str1.count("o",3,20))
# print(str1.count("to"))
# print(str1.count("to",3,10))


# string converstion

# str1="welcome TO python"
# var1 = str1.capitalize()
# print(var1)
# print(str1)
#
# print(str1.title())
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())
#
# print(str1.replace("python", "java"))
# print(str1.replace(" ", ""))
# print(str1.replace(" ", "", 1))
# str2="0012300"
# print(str2.strip("0"))
# print(str2.lstrip("0"))
# print(str2.rstrip("0"))

#################conv string to list

str1="apple orange kiwi"
print(str1.split())# default space
str1="apple, orange, kiwi"
print(str1.split())# default space
print(str1.split(", "))# default space

##############list to str
lst1=['apple', 'orange', 'kiwi']
print(", ".join(lst1))