# def keyword
# block of statemnet to do specicif task

# definition
#invoke func

# def myfunc():
#     print("this is my first function")
#
# print(myfunc)#<function myfunc at 0x000002EA9A4587C0>
# myfunc()

##########
# with parameter with return
# with parameter without return
# without parameter with return
# without parameter without return

######return statement

# def myfunc():
#     return "string"
#
# print(myfunc())
# or
# var=myfunc()
# print(var)

# def addition():
#     a=10
#     b=20
#     return a+b, a-b
#
# var=addition()# (30,-10)
# print(var[0])
# print(var[1])

# def myfunc():
#     print("this is statement")
#     return
# print(myfunc())


###################parament
# positional parameter
# keyword parameter

###################positional parameter

# def addition(a,b,c,d):
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")

# addition(1,2,3,4)
# addition(1,2,3)#TypeError: addition() missing 1 required positional argument: 'd'

#****Rule:
# def addition(a=0, b=0, c, d):
#
#     SyntaxError: non - default argument follows default argument

# def addition(a,b,c=0,d=0):
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")
#
# addition(1,2)
# addition(1,2, 3,4)
# # addition(1)#TypeError: addition() missing 1 required positional argument: 'b'


###################keyword parameter/arguments

# def addition(a,b,c,d):
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")
#
# addition(a=1, b=2, c=3, d=4)#a1+b2+c3+d4=10
# addition(c=3, d=4, a=1, b=2)#a1+b2+c3+d4=10
# addition(a=1, b=2)#TypeError: addition() missing 2 required positional arguments: 'c' and 'd'

# def addition(a,b,c=0,d=0):
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")

# addition(c=3, d=4, a=1, b=2)
# addition(a=1, b=2)

# addition(1,2,c=12,d=13)

#*****Rule2
#addition(a=1,b=2,12,13)
                          # ^
# SyntaxError: positional argument follows keyword argument
# addition(a=1,b=2,12,13)

# addition(1,2,a=12,b=13)#TypeError: addition() got multiple values for argument 'a'

######
# with parameter with return

# def printer(name):
#     return f"Hi, {name}"
#
# print(printer("john"))

# with parameter without return
# def printer(name):
#     print(f"Hi, {name}")
#
# printer("john")



# without parameter with return
# def printer():
#     name="john"
#     return f"Hi, {name}"
#
# print(printer())
# without parameter without return

# def printer():
#     name="john"
#     print(f"Hi, {name}")
#
# printer()

######scope of variable
# global var
# local var

x="Global variable"

def myfunc():
    y="Local Variable"
    print(f"inside myfunc x:{x} y:{y}")

# print(f"outside , before calling myfunc x:{x} y:{y}")#NameError: name 'y' is not defined
# myfunc()
# print(f"outside , after calling myfunc x:{x} y:{y}")#NameError: name 'y' is not defined