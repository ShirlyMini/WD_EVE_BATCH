# while
# range
# for

############################while loop
#1inti 2cond 3incre/decre
# print 1-10 num

# n=1# init
#
# while n<=10:# cond
#     print(n)
#     # n=n+1
#     n+=1# incre

# print 10-1 num

# n=10
# while n>=1:
#     print(n)
#     # n=n-1
#     n-=1# decr

# range func(start=0, end=n-1, incre/decr=1)
# print(list(range(10)))# starts from 0 ends with n-1
# print(list(range(5,10)))# starts from 5 ends with n-1
# print(list(range(5,10,2)))# [5, 7, 9]
# print(list(range(9,1,-1)))# [9, 8, 7, 6, 5, 4, 3, 2]
# print(list(range(9,1,-2)))# [9, 7, 5, 3]
# print(list(range(-8,7)))# [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]


# for loop
# print 1-10 num
# for var in range(1,11):
#     print(var)

# for var in range(10,0,-1):
#     print(var)

# for var in range(10):
#     print(var)

############################3Jumping statement (use along with if condition)

# break

# break when n =5

# n=1# init
#
# while n<=10:# cond
#     print(n)
#     if n==5:
#         break
#     # n=n+1
#     n+=1# incre

# for var in range(1,11):
#     print(var)
#     if var == 5:
#         break
    # break

# skip num divisble by 3

# continue

# n=0# init
#
# while n<=9:# cond
#     n += 1
#     if n%3==0:
#         continue
#     print(n)
#     # incre

for var in range(1,11):
    if var%3==0:
        continue
    print(var)