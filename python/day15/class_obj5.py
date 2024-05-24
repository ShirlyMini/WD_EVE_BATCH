# instance var
# constructor - instance method --def __init__(self) ---no return---invoked at the time of object creation

# class myclass:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         print("constructor ",self.a,self.b)
#
#     def func1(self):
#         print("func1",self.a,self.b)
#
#
#     def func2(self):
#         print("func2",self.a,self.b)
#
#     # @classmethod
#     # def func3(cls):
#     #     print("func3",cls.a,cls.b)
#     #
#     # @staticmethod
#     # def func4():
#     #     print("func3",a ,b)
#
# obj=myclass()
# obj.func1()
# obj.func2()
# # obj.func3()
# # obj.func4()

####################class myclass:
class myclass:
    def __init__(self, var1, var2):
        self.var1=var1
        self.var2=var2
        # print("constructor ",self.var1,self.var2)

    def func1(self):
        print("func1",self.var1,self.var2)


obj=myclass(10, 20)
obj1=myclass(100, 200)
obj2=myclass(1000, 2000)

obj.func1()
print(id(obj))
obj1.func1()
print(id(obj1))
obj2.func1()
print(id(obj2))