# import module1
# import module2
#
# module1.addition(1,2)
# module2.addition(10,20)

###from

# from module2 import addition
# from module1 import addition
#
# addition(1,2)


#######package- is collection of modules

# from pack1.module1 import printer_mod1
# from pack1.module1 import addition
# from pack1.module2 import *
# from pack1.pack2.module3 import *
# from pack1.pack2.module4 import *
#
# printer_mod1()
# printer_mod2()
# printer_mod3()
# printer_mod4()
# addition(1,3)


from pack1 import module1
from pack1 import module2
from pack1.pack2 import module3
from pack1.pack2 import module4

module1.printer_mod1()
module2.printer_mod2()
module3.printer_mod3()
module4.printer_mod4()
module1.addition(1, 3)
module2.addition(10, 30)
module3.addition(2, 3)
module4.addition(1, 5)

obj = module3.birds()
obj.name()