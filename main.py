import os
# *******************************slicing in list and strings*******************

# mylist=[0,1,2,3,4,5,6,7,8,9]
# print(mylist[1:])
# print(mylist[8:2:-1])
# print(mylist[::-1])
#
# stri='www.google.com'
# print(stri[-4:])
# print(stri[4:])
# print(stri[4:-4])


# ************************input and output**********************************

# name=input("enter the name :")
# print("hello",name)

# num1=int(input("enter 1st number :"))
# num2=int(input("enter 2nd number :"))
# x=num1//num2
# y=num1%num2
# print(num1+num2)
# print("the quotient of",num1,"and",num2,"is",x,"and remainder is",y)

# person = input('Enter your name: ')
# greeting = 'Hello, {}!'.format(person)
# print(greeting)

# person = input('Enter your name: ')
# print('Hello {}!'.format(person))

# a="hello"
# b="sachin"
# c="how are you"
# print("{} {} {}".format(a,b,c))

# a = 5
# b = 9
# setStr = 'The set is {{{}, {}}}.'.format(a, b)
# print(setStr)


# **************************sorting lists************************************


# li=[9,7,8,6,4,5,1,3,2]
# # sli=sorted(li)  #***************increasing order****************
# sli=sorted(li, reverse=True)  #***************decreasing order****************
# print("sorted list is :",sli)
#
# #li.sort()   #***************increasing order****************
# li.sort(reverse=True)
# print("orinal list is :",li)

# li=[-6,-4,-5,1,2,3]
# sli=sorted(li, key=abs)   #sorted according to absolute values
# print(sli)


# **************************sorting tuples************************************
# tup=(9,7,8,6,4,5,1,3,2)
# stup=sorted(tup)
# print("sorted touple is :",stup)


#***************************sorting dictionaries*****************************

# di={"name":"sachin","branch":"btech","friend":"harsh","gf":"monica"}
# sdi=sorted(di)
# print("sorted dictionary is :",sdi)

#********************sorting class objects***********************

# class Employee():
#     def __init__(self,name,age,salary):
#         self.age=age
#         self.name=name
#         self.salary=salary
#
#     def __repr__(self):
#         return "{}, {}, ${}".format(self.name,self.age,self.salary)
#
#
# e1=Employee("sachin", 21, 456321)
# e2=Employee("jp", 22, 23145)
# e3=Employee("ishant", 23, 12345)
#
# employ=[e1,e2,e3]
#
# def e_sort(emp):
#     return emp.salary
#
# semploy=sorted(employ, key=e_sort)
#
# print(semploy)

#************************input and rawinput***********************

# str1 = input("enter your input :")
# print(str1)

# **************************read and write file*********************

# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)

#*********************writing to a file***********************


# fo = open("foo.txt", "w")                 # Open a file
# str1="hello python !"
# fo.write(str1);
# fo.close()                                # Close opend file

#************************reading from a file**********************

# fo=open("foo.txt","r+")
# str1=fo.read(10);
# print("read data from file :",str1)
# pt=fo.tell();
# print("current file position :",pt)
# pos=fo.seek(0,0);
# str2=fo.read(10);
# print("again read data from file :",str2)
# fo.close()


#**************************renaming file**************************

# os.rename("foo.txt","file1.txt")

#**************************removing or deleting file*****************

# os.remove("file1.txt")

#*********************making directory*************************

# os.mkdir("newdir")                    #making new directory
# os.rmdir("newdir")                      #removing directory

#*******The getcwd() method displays the current working directory.********

# os.getcwd()

#***********************first class functions****************************

# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# def my_map(fun, arglist):
#     result = []
#     for i in arglist:
#         result.append(fun(i))
#     return result
#
# out=my_map(cube,[1,2,3,4,5])
#
# print(out)


#*******************************************************************

# def logger(msg):
#     def msg_logger():
#         print("hello",msg)
#     return msg_logger
#
# log=logger("sachin")
# log()

# def htmltag(tag):
#     def text(txt):
#         print("<{0}>{1}</{0}".format(tag,txt))
#
#     return text
#
# out=htmltag("h1")
# out("header")


#*******************************closure*********************************

# def outer_fun():
#     msg="hello"
#     def inner_fun():
#         print(msg)
#
#     return inner_fun
#
# out=outer_fun()
# out()

#****************************decorators**************************

def deco_fun(orig_fun):
    def wrap_fun():
        return orig_fun()
    return wrap_fun

def display():
    print("hello decorators")

out=deco_fun(display)
out()
