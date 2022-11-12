def filtering(li , filterKey):
    result = []
    for i in li:
        if len(result) == 0: 
            result.append({li[0][filterKey]:[i]})
        else: 
        
            if i["age"] in result[0].keys():
                result[0][i["age"]].append(i)
            else: 
                result[0][i["age"]] = [i] 
    return result
 




listOfDict = [{"name" : "Shahmeer", "age":24},
{"name" : "Maheer", "age":24},
{"name" : "Qasim", "age":24},
{"name" : "Shabana", "age":25},
{"name" : "Mudasir", "age":25}]

'''
--> [{24:[{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24},{"name" : "Shahmeer", "age":24}] ,
 25: [{"name" : "Shabana", "age":25}, {"name" : "Shabana", "age":25}] }]

'''
print(filtering(listOfDict,"age"))