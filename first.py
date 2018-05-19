# #a=int(input("enter the 1st value :"))
# #b=int(input("enter the 2nd value :"))
# #c=int(input("enter the 3rd value :"))
# #print("result is :")
# #print(max(a,b,c))
# #print("hola")
#
# #strings
#
# #a='hello is a don\'t string '
# #b="hello this is a string"
# #c="hello \\is a string"
# #d="hello "
# #e=5
# #print(len(a))
# #print(a+b)
# #print(c)
# #print(d * 10)
# #print(d + str(e))
#
# names=["sachin","dk","suraj"]
# names.append("jp")
# ages=[12,13,14,15]
# print(names[0] +" "+ names[1])
# names.extend(ages)
# names.remove("dk")
# print(names)
# print(names, ages)
#
# #list=[1,2,3,4,5,6,7,8,9]
#
# #print(list[0:10:2])
#
# #n=int(input("number :"))
# #if n<0:
# #    print("absolute no of ",n," is",-n)
# #else:
# #    print("absolute no of ",n," is",n)
#
# name=input("number :")
# if name=="sachin":
#    print("enterd name is ",name)
# elif name=="jp":
#    print("enterd name is ",name)
# elif name=="ishant":
#    print("enterd name is ",name)
# else:
#    print("enterd name is invalid")
#
#
# # name="animals"
# # animal_name="frog"
#
# # if name=="animal":
#     # if animal_name=="dog":
#         # print("valid animal")
#     # else:
#         # print("not a valid animal")
# # else :
#     # print("hola")
#
#
# if (1<3 and 3<5):
#     print("yes")
# else :
#     print("no")
#
# # while loop
#
# # a=0
# # while a<5:
# #     print(a)
# #     a+=1
#
# # a=1
# # s=0
# # while (a!=0):
# #     print('current sum ',s)
# #     a=float(input('number ?'))
# #     s+=a
# # print('total sum ',s)
#
# # a=[1,2,3,4,5,6,7,8,9,10]
# # for num in a:
# #     print(num)
#
# # functions
#
# def hello(x):
#     print("hello",x)
# hello("papa")
#
# # def sum(x,y):
# #     return(x+y)
# # sum1=sum(2,5)
# # print(sum1)
#
# # default perametrers
#
# def sscore(name="tom",score=0):
#     print(name,"scored",score, "marks")
# sscore()
# sscore("sachin",100)
# sscore("dk")
# sscore(score=99)
#
# # multiple perametrers
# def sscore(name,*score):
#     print(name)
#     print(score)
# sscore("rohan",12,45,7,8)

#
# # classes
# class Person:
#     def setname(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def showname(self):
#         print(self.fname, self.lname)
#
# pp=Person()
# pp.setname("rahul","khanna")
# pp.showname()
#
#
# # constructors and destructors
#
# class Person:
#     def __init__(self):
#         print("class is created")
#     def __del__(self):
#         print("class obeject is destoyed")
#     def setname(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def showname(self):
#         print(self.fname, self.lname)
#
# pp=Person()
# pp.setname("rahul","khanna")
# pp.showname()
#
#
# # inheritance in classes
#
# class Parent:
#     value1=12
#     value2=15
# class Child(Parent):
#     pass
#
# parent1=Parent()
# print(parent1.value1)
# chlid1=Child()
# print(chlid1.value2)

# print("hello sachin, welcome back")
