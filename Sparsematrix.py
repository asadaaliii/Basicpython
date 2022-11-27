# matrix= [[0,0,0,1,0],
#          [2,0,0,0,3],
#          [0,0,0,4,0]]
# mat= {(0,3):1,(1,0):2,(1,4):3,(2,3):4}
# # print(mat[0,3])
#
# print(mat)
# print(mat.get((0,3),0))
# print(mat.get((0,1),0))
# print(mat.get((1,2),0))
# print(mat.get((1,4),0))
#
# m = { }
# for x in "mississippi":
#     m[x]=m.get(x,0)+1
# print(m)


# lst = [1,2,3,4,5,]
# lst2 = lst
# print(lst2)
# lst[2]=10
# print(lst)

opposites = {'up':'down','right':'wrong','true':'false'}
alias=opposites
print(alias is opposites)
print(opposites is alias)
alias['right']='left'
print(alias)
print(opposites['right'])
