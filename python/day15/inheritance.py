## class A(func1, func2) and class b(finc3)

###parent class, super, base
###child class, derived class, sub class
# 4 types of inhertaince
#1. single inheritance
# class A:
#     def funcA(self):
#         print("FuncA of A")
#
# class B(A):
#     def funcB(self):
#         print("FuncB of B")
#
# obj=B()
# obj.funcA()
# obj.funcB()


#2. multiple inheritance
# class A1:
#     def funcA1(self):
#         print("FuncA of A1")
#
# class A2:
#     def funcA2(self):
#         print("FuncA of A2")
#
# class B(A1, A2):
#     def funcB(self):
#         print("FuncB of B")
#
# obj=B()
# obj.funcA1()
# obj.funcA2()
# obj.funcB()

# multilevel

# class A1:
#     def funcA1(self):
#         print("FuncA of A1")
#
# class A2(A1):
#     def funcA2(self):
#         print("FuncA of A2")
#
# class B(A2):
#     def funcB(self):
#         print("FuncB of B")
#
# obj=B()
# obj.funcA1()
# obj.funcA2()
# obj.funcB()

# hirerchical
#
# class A:
#     def funcA(self):
#         print("FuncA of A")
#
# class B1(A):
#     def funcB1(self):
#         print("FuncAB1 of B1")
#
# class B2(A):
#     def funcB2(self):
#         print("FuncB2 of B2")
#
# obj=B1()
# obj.funcA()
# obj.funcB1()
#
# obj=B2()
# obj.funcA()
# obj.funcB2()

############################
class A0:
    def funcA0(self):
        print("FuncA0 of A0")
class A(A0):
    def funcA(self):
        print("FuncA of A")

class B1(A):
    def funcB1(self):
        print("FuncAB1 of B1")

class B2(A):
    def funcB2(self):
        print("FuncB2 of B2")