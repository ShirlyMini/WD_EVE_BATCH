# +--operator overloading
# print(10+10)
# print("str"+"str")
# print(["str"]+["str"])
# # *--operator overloading
# print("str"*10)
# print(["str"]*10)

#func overloading
# func overriding-NA

# def func():
#     print("func 1")
#
# def func():
#     print("func 2")
#
# def func():
#     print("func 3")
#
# func()
#
# class myclass:
#     def func(self):
#         print("func 1")
#
#     def func(self):
#         print("func 2")
#
#     def func(self):
#         print("func 3")
#
# obj=myclass()
# obj.func()

# func overloading

# def func(a,b,c):
#     print(a,b,c)
#
# func(10,20,30)
# func(10,20,30, 40)

##*args and **kwargs(variable length parameter)


# def func(*args):#will accept more than 2
#     print(args)# tuple
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#
#
# func(10,20,30,40,60,70,80)


def func(**kwargs):#will accept more than 2
    print(kwargs)# dictiona
    sum=0
    for i in kwargs.values():
        sum=sum+i
    print(sum)


func(a=10,b=20,c=30,d=40,e=60,f=70,g=80)
func(a=10,b=20,c=30,d=40)