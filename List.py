                         # List

# list= ["ABC","XYZ" ,10,11]
# print(list[2])
#
# list = ["apple", "banana" , "cherry"]
# print(list[0])
# print(list[0:])
# print(list[:])
# print(list[1:2])

# l = ['foo','bar','baz','qux','quux','corge']
# print(l[0:2:1])
#
# l = ['foo','bar','baz','qux','quux','corge']
# print(l[:-5:-1])

# list= ["apple","banana","cherry"]
# n = str(input("type name "))
# if n in list:
#     print("yes" , n, "is in the list.")
# else:
#     print("Sorry, 'it is not in the list.'")


# #replace
# list = ["apple","mango","banana"]
# list[1]="asad"
# print(list)

#change a range
# list = ["apple","banana","mango","cherry","orange","kiwi"]
# list[1:3]=["blackcurrant","watermelon"]
# print(list)

# list = ["apple","banana","cherry"]
# list[1:2]=["blackcurrant","watermelon"]
# # print(len(list))
# print(list)

# list1 = ["apple","banana","cherry"]
# list2 = ["1","5","6","7"]
# list3 = ["True" , "False"]
# print(type(list))
# print(len(list3))


# list = ["asad","harsh","ajay","sarthak","diya","Harsh",]
# if "Ali" in list:
#     print("Yes", "it is available here")
# else:
#     print("no")

# list = ["as","ad","ali"]
# list[1] = "Asad"
# print(list)


# list=["apple","banana","cherry","orange","kiwi","mango"]
# list[1:3] = ["blackcurrent","watermelon"]
# print(list)
# print(len(list))

# list = ["apple","banana","cherry"]
# list[1:2] = ["watermelon", "kiwi"]
# print(len(list))
# print(list)

# list = ["apple","banana","cherry"]
# list[1:3] = ["watermelon"]
# print(len(list))
# print(list)

# letters = "abcdefghijklmnopqrstuvwxyz"
# string_letters = str(letters)
# lists_letters = list(letters)
# tuples_letters = tuple(letters)
# sets_letters = set(letters)
#
# print("String: ",string_letters)
# print("lists: ",lists_letters)
# print("tuples: ",tuples_letters)
# print("Sets: ",sets_letters)

# setal = "Asad Ali"
# a = set(setal)
# print(a)

# ali = ["harsh" ,"ajay" , "diya" , "asad" , "vikash" , "ritik"]
# ali.append("Sarthak")
# print(ali)

# ali.clear()
# print(ali)

# ali.copy()
# print(ali)


# list=["apple","banana","cherry","orange","kiwi","mango"]
# list.append("ajay")       #only one element can be added
# print(list)

# list=[12,32,25,56,73,45,83,18]
# list.clear()
# print(list)
# list.append(10)
# print(list)
# list.append(45)
# print(list)

# list=[12,32,25,56,73,45,83,18]
# x= list.copy()
# print(x)
# x.append(17)
# print(x)
# print(list)

# list=[12,32,25,56,12,73,45,12,83,18]
# x=list.count(12)
# print(x)
# print(len(list))

# list=[12,32,25,56,73,45,83,18]
# list.extend((12,'asad'))
# print(list)
# list.extend(['a','b','c'])
# print(list)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# x = list.index((14))
# print(x)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# list.insert(4,'Hello')
#   print(list)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# list.pop()
# print(list)
# x=list.pop(2)
# print(x)
# print(list)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# list.remove(12)
# print(list)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# list.reverse()
# print(list)

# list=[12,32,14,25,56,12,14,73,45,12,83,18]
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# list=['Harsh','ajay','diya','Asad']
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

                                    #Comprehesion

# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x   )
# print(newlist)


                                        #List List Comprehension

# newlist = [x for x in range(10)]
# print(newlist)
# [0,1,2,3,4,5,6,7,8,9]

# nlist = [x for x in range(10) if x<5]
# print(nlist)


# square = list(map(lambda x: x**2, range(10)))
# print(square)
#
# sq = [x**2 for x in range(10)]
# print(sq)

# newlist = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(newlist)
# ali = newlist[0]
# print(ali)
# print(type(ali))

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
# print([[row[i] for row in matrix] for i in range(4)])
# print(type(matrix))
# print(len(matrix))



