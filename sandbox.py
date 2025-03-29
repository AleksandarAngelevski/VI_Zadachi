# # state =("h1","h2")

# # ho = state[0],state[1]
# # actions = {"Gore 1":(0,1),"Gore 2":(0,2),"Gore 3":(0,3),"Desno 1":(1,0),"Desno 2":(2,0),"Desno 3":(3,0),}
# # for key in actions.keys():
# #     print(key)

# line = "3,2,1;;"
# lista =[]
# for i in line.split(';'):
#     tempList = []
#     for j in i.split(','):
#         tempList.append(j)
#     lista.append(tempList)

# output = tuple([tuple(list_item) for list_item in lista])
# print(output)
# print([list(el) for el in output])





# def emptyTuples(topka):
#     l =  0
#     indexesList=[]
#     for i in range(len(topka)):
#         if(len(topka[i])!=0 and topka[i][0] !=''):
#             l+=1
#             indexesList.append(i)
#     return (l,tuple(indexesList))
# x = emptyTuples(output)

# print([list(l) for l in ((5,),('',),(1,))])

# l = ['']
# print(l[-1] + " +")


list1 = [[1]]
list2 = list(list1)

print(((3,2,1),('',),('',))==((3,2,1),('',),('',)))

torka = ((1,2),(3,4))
torka2 = ((4,3),(2,1))



