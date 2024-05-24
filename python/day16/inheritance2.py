# multiple inheritance
# class parent1:
#     def func(self):
#         print("this is parent1 func1")
#
# class parent2:
#     def func(self):
#         print("this is parent2 func2")
#
# class child(parent2, parent1):# MRO-child class
#     def func3(self):
#         print("this is child func3")
#
# obj=child()
# obj.func()


# class parent:
#
#     def func(self):
#         print("this is func from parent class")
#
#     def func1(self):
#         print("this is func1 from parent class")
#
#     @classmethod
#     def func1_class(cls):
#         print("this is class func1 from parent class")
#
#     @staticmethod
#     def func1_static():
#         print("this is static func1 from parent class")
#
# class child(parent):
#     def func(self):
#         print("this is func from child class")
#
#     def func2(self):
#         print("this is func2 from child class")
#
#     def child_func(self):
#         print("this is child func from child class")
#         self.func()
#         parent.func(self)
#         self.func2()
#         self.func1()
#         self.func1_class()
#         self.func1_static()
#
# obj=child()
# obj.child_func()


#####constuctor

class parent:
    def __init__(self,a,b):
        print("constructor from parent class",a,b)

    def parent_func(self):
        print("this is func from parent class")

class child(parent):
    def __init__(self,a,b, c,d):
        print("constructor from child class",a,b)
        # parent.__init__(self)
        #self.__init__()#RecursionError: maximum recursion depth exceeded while calling a Python object
        super().__init__(c,d)# super class refers to parent class

    def child_func(self):
        print("this is child func from child class")


obj=child(10,20,30,40)
