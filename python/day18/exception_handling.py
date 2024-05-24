# import builtins
#
# print(dir(builtins))#['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# print(10+"10")


# try:
#     # l1=[1,2,3,4,5]
#     # print(l1[6])
#     print(10 + "10")
# except IndexError as msg:
#     print("Index Error happened",msg)
# except TypeError as msg:
#     print("Type ERROR happened", msg)


# try:
#     l1=[1,2,3,4,5]
#     print(l1[6])
#     # print(10 + "10")
# except Exception as msg:
#     print("some Error happened", msg)


#######
# if year != leap year error should happen

# user induced exception
#raise
# assert

# n=2001
# if n%4==0:
#     print("leap year")


#####################3raise

# raise Exception("This is user induced exception")
# raise TypeError("This is user induced exception")


# try:
#     n=2005
#     if n%4==0:
#         print("leap year")
#     else:
#         raise AttributeError("Not leap year")
# except AttributeError as msg:
#     print("ERROR:", msg)

########################assert

# assert True, "some error happened"# no error happen
# assert False, "some error happened"# error will happen

# assert 3<4, "some error happened"
# try:
#     n=2001
#     assert n%4==0, "not leap year"
# except AssertionError as msg:
#     print("ERROR:", msg)


######################### optional block else and finally

try:
    #a=10
    print(a)# name
except Exception as msg:# when there is exception
    print("error handled!!!", msg)
else:# when there is no exception
    print("no Exception happened")
finally:# cleanup
    print("Always executed")
