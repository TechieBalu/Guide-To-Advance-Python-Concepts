# def filtering(li , filterKey):
#     result = []
#     for i in li:
#         if len(result) == 0: 
#             result.append({li[0][filterKey]:[i]})
#         else: 
        
#             if i["age"] in result[0].keys():
#                 result[0][i["age"]].append(i)
#             else: 
#                 result[0][i["age"]] = [i] 
#     return result
 




# listOfDict = [{"name" : "Shahmeer", "age":24},
# {"name" : "Maheer", "age":24},
# {"name" : "Qasim", "age":24},
# {"name" : "Shabana", "age":25},
# {"name" : "Mudasir", "age":25}]

# '''
# --> [{24:[{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24}] ,
#  25: [{"name" : "Shabana", "age":25}, {"name" : "Shabana", "age":25}] }]

# '''
# print(filtering(listOfDict,"age"))



property_lists = [['Semi-Detached', '|', '', '2', '|', '', '2'], ['Detached', '|', '', '5', '|', '', '3'], ['Detached', '|', '', '5', '|', '', '5']]

propertyList1 = [items for items in property_lists[0]]
propertyList2 = [items for items in property_lists[1]]
propertyList3 = [items for items in property_lists[2]]

print(propertyList1)
print(propertyList2)
print(propertyList3)