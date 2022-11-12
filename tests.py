
# def filtering(l1, filteroutKey):
#     result = []
#     count = 0
#     keysList = []
#     for i in l1: 

#         age = i[filteroutKey]

        
#         if len(result) == 0:
#             dic = {age:[i]}
#             result.append(dic)

#         else: 
#             result[0]

#                 # keysList.append(i.keys())


#         else:
#             keys = result[0].keys()


#             if age not in keys:
#                 dic = {age:[i]}
#                 result.append(dic)
#             else: 
#                 # print("in i=else")
#                 for i in result:
#                     if age in i.keys():
#                         l = result[0][age]
#                         # print(l)
#                         l.append(i)
#                         # listOfKeys.append()
#         count +=1
#     return result



listOfDict = [{"name" : "Shahmeer", "age":24},
{"name" : "Maheer", "age":24},
{"name" : "Qasim", "age":24},
{"name" : "Shabana", "age":25},
{"name" : "Mudasir", "age":25}]

# '''
# --> [{24:[{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24}] ,
#  25: [{"name" : "Shabana", "age":25}, {"name" : "Shabana", "age":25}] }]

# '''
# print(filtering(listOfDict,"age"))

# # keys = listOfDict[0].keys()
# # print("age" in keys)

for i in listOfDict[0].keys():
    print(i)
print(type(listOfDict[0].keys()))