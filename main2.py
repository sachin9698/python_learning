
#************************iterators*******************************

# lis=[1,2,3,4,5]
#
# # literator=iter(lis)
# #
# # print(next(literator))
# # print(next(literator))               #both works the same
# # print(literator.__next__())


#***********************iterator in for loop**********************


# lis=[1,2,3,4,5]
#
# for element in lis:
#     print(element)


#************************generators*********************************

# def my_gen():
#     n=1;
#     print("this is printed first !")
#     yield n
#
#     n=n+1
#     print("this is printed second !")
#     yield n
#
#     n=n+1
#     print("this is printed second !")
#     yield n

# a=my_gen()
# next(a)
# next(a)
# next(a)

#uisng for loop

# for elem in my_gen():
#     print(elem)


#eg-2

# def str_rev(str):
#     l=len(str)
#     for i in range(l-1,-1,-1):
#         yield str[i]
#
# for char in str_rev("hello"):
#     print(char)

#eg-3

def pow(max=0):
    n=0
    while n<max:
        yield 2**n
        n=n+1

a=pow(max=5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
