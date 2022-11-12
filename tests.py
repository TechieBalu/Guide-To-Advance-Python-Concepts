
def filtering(l1, filteroutKey):
    listOfKeys = []
    count = 0
    for i in l1: 

        age = i[filteroutKey]
        

        if count == 0:
            dic = {age:[i]}
            listOfKeys.append(dic)
        else:
            keys = listOfKeys[0].keys()
            if age not in keys:
                dic = {age:[i]}
                listOfKeys.append(dic)
            else: 
                # print("in i=else")
                for i in listOfKeys:
                    if age in i.keys():
                        l = listOfKeys[0][age]
                        # print(l)
                        l.append(i)
                        # listOfKeys.append()
        count +=1
    return listOfKeys



listOfDict = [{"name" : "Shahmeer", "age":24},
{"name" : "Maheer", "age":24},
{"name" : "Qasim", "age":24},
{"name" : "Shabana", "age":25},
{"name" : "Mudasir", "age":25}]


print(filtering(listOfDict,"age"))

# keys = listOfDict[0].keys()
# print("age" in keys)


