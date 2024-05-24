# mem allocation
#static and dynamic

# static mem===[stack--limited mem]
# var cration, print all exe are static

# dynamic  == heap - unlimited
# func, obj
# v=12
# print(v)
# def myfunc(a):
#     print(a)
#
# myfunc(1)
# myfunc(2)


# class myclass:
#     # print("this is my first class craetion")
#     v=10
#     print(v)# 4
#     # print(id(v))
#
#     def func1(self):# instance method# default
#         # self repr obj
#         # rule self as first
#         print(f"inside func1 {self}")
#         print("this is func1")
#
#     def func2(self, a, b):
#         print("this is func2")
#         print(f"a{a}b{b}")
#
#
#
# # obj
# # physical entity
# # mem allcation will happen
# # object creation - instance or instanciation
# obj=myclass()#instanciation
# print(f"after creating obj {obj}")
# # print(obj.v)
# # print(id(obj.v))
# # obj.v=100
# # print(obj.v)
# # print(id(obj.v))# dynamic mem
#
# obj.func1()# backend iterpreter will pass obj as first parament
# # obj.funasxsadc1()# AttributeError: 'myclass' object has no attribute 'funasxsadc1'
# # obj.func1(1)# TypeError: myclass.func1() takes 1 positional argument but 2 were given
# obj.func2(2, 1)
# # obj.func2(2)#TypeError: myclass.func2() missing 1 required positional argument: 'b'


######


# class myclass:
#     # print("this is my first class craetion")
#     v=10
#     # print(v)# 4
#     # print(id(v))
#
#     def func1(self):# instance method# default
#         # self repr obj
#         # rule self as first
#         print(f"inside func1 {self}")
#         print("this is func1")
#
#     def func2(self, a, b):
#         print("this is func2")
#         print(f"a{a}b{b}")

# print(myclass)#<class '__main__.myclass'>
# print(myclass.v)
# print(id(myclass.v))
# myclass.v=100
# print(myclass.v)
# print(id(myclass.v))
#
# myclass.func1(1)
# myclass.func2(1,2,3)

# a=10
# print(id(a))
# a=100
# print(id(a))

#################################class
