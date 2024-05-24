# test data
# logs

# file handling- 3 mode
# read(default)
# write
# append

# open
##################################
# write

# if the file is present - content overwrite
# if the file is not present - cretes the file and writes the content

# fh = open("./test1.txt","w")
# fh.write("statement 5\n")
# fh.write("statement 6\n")
# fh.write("statement 7\n")
# fh.write("statement 8\n")
#
# fh.close()

####with statment(saves automaticaly)

# with open("./test1.txt","w") as fh:
#     fh.write("statement 9\n")
#     fh.write("statement 10\n")
#     fh.write("statement 11\n")
#     fh.write("statement 12\n")


##################################
# append

# if the file is present - content append
# if the file is not present - cretes the file and writes the content

# fh = open("./test2.txt", "a")
# fh.write("statement 1\n")
# fh.write("statement 2\n")
# fh.write("statement 3\n")
# fh.write("statement 4\n")
# fh.close()

########with statement

# with open("./test2.txt", "a") as fh:
#     fh.write("statement 1\n")
#     fh.write("statement 2\n")
#     fh.write("statement 3\n")
#     fh.write("statement 4\n")
#     # print(fh.read())#io.UnsupportedOperation: not readable


########read

# read(default)
# should take only exsisting file

# open("./test1.txt", "r")
# fh = open("./test1.txt")
# print(fh.read())

# print(fh.readline())
# print(fh.readline())
# print(fh.readline())
# print(fh.readline())

# print(fh.readlines())




# fh.write(";kssmxoksxoi")#io.UnsupportedOperation: not writable
# fh.close()
#FileNotFoundError: [Errno 2] No such file or directory: './testkmwlkm.txt'

#######with

with open("test1.txt") as fh:
    print(fh.read())
