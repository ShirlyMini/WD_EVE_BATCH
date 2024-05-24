# global- accessible all over the program
#local- accessible inside the func
# Ex1
# x="global var"
#
# def myfunc():
#     y="local var"
#     print(f"X:{x} and Y:{y}")
#
# print(f"X:{x} and Y:{y}")#NameError: name 'y' is not defined
# myfunc()
# print(f"X:{x} and Y:{y}")#NameError: name 'y' is not defined

######Ex2

# x="global var"
#
# def myfunc():
#     x="local var"
#     print(f"X:{x}")
#
# myfunc()
# print(f"X:{x}")


######Ex3

a=1
def myfunc():
    global a
    a=2
    print(f"inside func A:{a}")

print(f"outside before calling func A:{a}")#1
myfunc()
print(f"outside after calling func A:{a}")#2

####ex4 ERROR scenario

# a=1
# def myfunc():
#     a=2
#     global a#SyntaxError: name 'a' is assigned to before global declaration
#     print(f"inside func A:{a}")
#
# print(f"outside before calling func A:{a}")# 1
# myfunc()
# print(f"outside after calling func A:{a}")#1

##########ex5 EEROR scenario

# a=1
# def myfunc():
#     print(f"inside func A:{a}")
#     a=2#UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#     print(f"inside func A:{a}")
#
# print(f"outside before calling func A:{a}")# 1
# myfunc()
# print(f"outside after calling func A:{a}")#1