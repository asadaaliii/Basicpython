#Auther :- Asad Ali
#python Classroom
# nums = [ ]
# nums.append("Asad Ali")
# nums.append(19)
# nums.append(20.00)
# print(nums)
# number1 = int(input("Enter your number1:- "))
# number2 = str(input("Enter your word:- "))
# number3 = number1,number2
# print("Product is ",number3)
# number1 = 20
# if (number1<12):
#     print("number1 is good")
# elif (number1>51):
#     print("number1 is not good")
# else:
#     print("number1 is Great")
# n = "Asad Ali"
# print("My name is :- ", n , "and I belongs to Section:- K22BT" "*+/")
# n = input()
# print("my name is :-" , n)
# n = input("What is your name?" )
# print("My Name is :- ",n)
# a = input("Enter Your Age:-")
# print("My name is :-",n ,"and My age is:-"+a)
# print(type(a))
# Name = input("Please Enter your name :-")
# Age = input("And Also Please Enter Your Age :-")
# City = input ("And ENter your City Name:-")
# print("Name is :-",Name, "\nAge is :- "+Age,"\nAnd Your City is :-",City)

# a = "15"
# a = 15.20
# b = "Asad ALi"
# print(str(a) , b)
# print("Name is :-",Name, "\nAge is :- "+Age,"\nAnd Your City is :-",City)
#OPRETORS
# = is assigment opretor
#logical opretors :- and ,or ,not
# print(5==2)
# print(5==5)
# print(0 and 0)
# print(0 and 5)
#not is only for one digit
# print(not 0)
# print( not 12)
# print (5 and 1)
# print (5 and 0)
# print (5 or 1)
# print (565869554 or 0)
# print (5>2)
# print("Asad Ali " * 5)
# import keyword
# print(keyword.iskeyword("in"))
#operation on String
# x = len("Hello")
# print(x)
# x = "HELLO"
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[0:2])
# print(x[0:3])
# print(x[0:4])
# print(x[0:5])
# print(x[0:6])
# S - name [start index : stop ind. : step]
# a = "ASAD ALI"
# print(a[0:8:4])
# print(a[0:8:1])
# print(len(a))
# x = "ABC XYZ"
# print(len(x))
#  print(x[0:6])
#  print(x[0:7])
# print(x[:])
# print(x[:5])
# print(x[:4:2])
# print(x[: :2])
# print(x[: :1])
# s = "Welcome to LPU"
# print(len(s))
# print(s[5])
# print(s[0:5])
# print(s[0:14:2])
# print(s[: : 1])
# print(s[-14:-8])
# print(s[-14:-8:1])
# print(s[-7:-1])
# print((s[-7:-1:3]))
# print(s[-14:-8:-1])
# print(s[-7:-14])
# print(s[-14:-1])
# print(s[: :-1])
# print(s[-9:-2])
# print(s[-3:-11:-1])
# print(s[-5:-1])
# print(s[-5:])
# print(s[ : :-1])
                                      # detail about the placeholders
# txt1 = "My name is {fname},I am {age}". format(fname="Asad", age= 18)
# print(txt1)
# txt2 = "My name is {0},I am {1}".format ("asad" , 18)
# print(txt2)
# txt3 = "My name is {}, I'm {}".format("Asad Ali",18)
# print(txt3)
# x = "asad"
# print(x.capitalize())
# print(x.casefold())
# print(x.center(15))
# n = int(input("n = "))
#                              #for even number condition
# if n%2!=0:
#     print("the number is odd")
# else:
#     print("the number is even")
# n = float(input("age:- "))
# if n<4:
#     print("infant")
# elif n>=4 and n<11:
#     print("child")
# elif n>=11 and n<18:
#       print("teenager")
# else:
#      print("adult")
                            # leap year finding codes
# y = int(input("Type your year:-"))
# if y%4==0:
#     print("leap year")
# else :
#     print("not leap year")
#
# y = int(input("Type centennial year"))
# if y %400==0:
#     print("centennial year"
#           )
# else :
#     print("leap year")
# y = int(input("Which year? "))
# if y % 4:
#     print("no leap yaer")
# elif y % 100==0 and y % 400 !=0:
#     print("no leap year")
# else :
#     print("leap year")
                                                    #ITERATION
# i=1
# while i<71:
#     print(i)
#      i=i+1
#print("Bye")
# i = 1
#
# while i<10:
#     # n = input("Enter Your Name :- ")
#     print(i,n)
#     i=i+1
# print(range(5,20,2))
# i = 0
# while i in range(0,10):
#     print(i)
#     i = i + 1
# a = int(input("what is you number? "))
# i = 0
# while a in range (50):
#      if (a%2==0):
#         print(a,'even')
#      else :
#         print(a,'odd')
#         i = i + 1

                           # FOR LOOP count
# count_o=0
# count_e=0
# for i in range(0,10):
#     if (i%2==0):
#         print(i,"is even")
#         count_e=count_e+1
#     else:
#          print(i,"is odd")
#          count_o=count_o+1
#         #count_e+=1 it is also use for counting
# print("total even",count_e)
# print("total odd",count_o)

# i=0
# while i <10:
#     if(i==6):
#         continue
#     print(i)
#     i=i+1
# print("Thank you")

# i=0
# while i<10:
#     if i==4 or i==5 or i==8:
#         i+=1
#         continue
#     else:
#          print(i)
#          i+=1

# i=0
# while i<10:
#     if i==4 or i==5 or i==8:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
# print("tq")

# i=-1
# while i<9:
#     i=i+1
#     if i==4:
#         continue
#     elif i==5:
#         continue
#     elif i==8:
#         continue
#     print(i)


# i=0
# while(i<=9):
#     if(i==4):
#         i+=2
#         continue
#     elif (i==8):
#         i=i+1
#     print(i)
#     i+=1

                # for loop using

# for i in range(0,10):
#     if(i==4) or (i==5) or (i==8):
#         continue
#     print(i)

                 #reversed range

# for i in  reversed(range(10,21)):
#     print(i)
      #PEMDAS  using in large equations.



















