import re,os
import Licenses
import tokenizer


def cleanUp(commentsListFromTokenizer):
    result = " ".join(commentsListFromTokenizer)
    return result

def generalizedLicenseExtraction(text):
    license = Licenses.licenses
    results = []
    for i in license: 
        licenseName = i["licenseName"]
        licenseId = i["licenseId"]
        regexForLicenseExtraction = f'(The)?\s+({licenseName}|{licenseId})\s+'
        pattern = re.compile(regexForLicenseExtraction, re.I|re.M)
        match = pattern.finditer(text)
        results.append(match)
    
    return results


def licenseRefiner(match,text):
    result = []
    licensesFound = []
    for callable_iterator in match:
        for i in callable_iterator:
            try:
                span = i.span()
                result.append(text[span[0]:span[1]])
            except:
                continue

    if result == []:
        # print("NO MATCH FOUND")
        return None
    
    else:
        # print("results",result)
        for i in result:
            # print(i)
            j = i.replace('\n',"")
            # pattern = re.compile()
            licensesFound.append(j)
        
        if licensesFound == []:
            return "No License found"
        return licensesFound



def initiator(filePath):
    tokenized = tokenizer.tokenizer(filePath)
    cleanedCode = cleanUp(tokenized)
    print("\n\n------------------------------ Licenses ---------------------------------")
    match = generalizedLicenseExtraction(cleanedCode)
    print(licenseRefiner(match , cleanedCode))



initiator(r"D:\2022\Python Practice\Regex\test.java")