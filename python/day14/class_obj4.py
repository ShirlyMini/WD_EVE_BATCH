# global var
# local var
# class var
# instance variable
# x="GLOBAL"
#
# class myclass:
#     y="CLASS"
#
#     def func1(self):
#         z="LOCAL"
#         print(f"global variable {x}")
#         # print(f"class variable using self {y}")#NameError: name 'y' is not defined
#         print(f"class variable using self {self.y}")
#         print(f"class variable using class name {myclass.y}")
#         print(f"local variable {z}")
#
# obj=myclass()
# obj.func1()


################################################
# x="GLOBAL"

# class myclass:
#     x="CLASS"
#
#     def func1(self):
#         global x# conv local to global
#         x="LOCAL"
#         print(f"global variable {globals()['x']}")
#         # print(f"class variable using self {y}")#NameError: name 'y' is not defined
#         print(f"class variable using self {self.x}")
#         print(f"class variable using class name {myclass.x}")
#         print(f"local variable {x}")
#         #return x
#
# obj=myclass()
# # print(x)
# # obj.func1()
# # print(x)
#
# ########
# print(x)
# print(obj.x)
# obj.func1()
# print(x)

##############################class method
# x="GLOBAL"
#
# class myclass:
#     x="CLASS"
#
#     @classmethod
#     def func1(cls):
#         global x
#         x="LOCAL"
#         print(f"global variable {globals()['x']}")
#         print(f"class variable using self {cls.x}")
#         print(f"class variable using class name {myclass.x}")
#         print(f"local variable {x}")
#
# obj=myclass()
# # obj.func1()
# ########
# print(x)
# print(obj.x)
# print(myclass.x)
# obj.func1()
# print(x)


#####################################static

x="GLOBAL"

class myclass:
    x="CLASS"

    @staticmethod
    def func1():
        global x
        x="LOCAL"
        print(f"global variable {globals()['x']}")
        print(f"class variable using class name {myclass.x}")
        print(f"local variable {x}")

obj=myclass()
# obj.func1()
########
print(x)
print(obj.x)
print(myclass.x)
obj.func1()
print(x)