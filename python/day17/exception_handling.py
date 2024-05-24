# types of error

# error-- syntax and indent
# expection error - logical--handle

# if a:#SyntaxError: expected ':'
# print("hi")#IndentationError: expected an indented block after 'if' statement on line 6


# print("statement1")
# print("statement2")
# print("statement3")
# print("statement4")
# print(a) # terminate #NameError: name 'a' is not defined
# print("statement5")
# print("statement6")
# print("statement7")
# print("statement8")
# print("statement9")


print("statement1")
print("statement2")
print("statement3")
print("statement4")
try:
    #a=10
    print(a)# name
except Exception as msg:
    print("error handled!!!", msg)
print("statement5")
print("statement6")
print("statement7")
print("statement8")
print("statement9")