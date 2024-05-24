# data hiding or data abstartion
# public(default), private , protected(psuedo protected)

class myclass:
    var1="public variable"
    __var2="private variable"
    _var3="protected var"

    def func1(self):
        print("this is public method")

    def __func2(self):
        print("this is private method")

    def _func3(self):
        print("this is protected method")

    def func_to_access_pvt_attr(self):
        print(self.__var2)
        self.__func2()



obj=myclass()
print(obj.var1)
obj.func1()
obj.func_to_access_pvt_attr()

print(obj._var3)
obj._func3()

