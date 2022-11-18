import os , re 
import pygments
import pygments.token
import pygments.lexers



def tokenizer(filePath):

    # file = open(filePath, "r")
    # text = file.read()
    # file.close()
    print(filePath)
    with open(filePath, 'r' ,encoding='utf-8' , errors='ignore') as f:
        text = f.read()
    lexer = pygments.lexers.guess_lexer_for_filename(filePath, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    count1 = 0    #tag to store corresponding position of each element in original code file
    count2 = 0    #tag to store position of each element in cleaned up code text
    # these tags are used to mark the plagiarized content in the original code files.
    for i in range(lenT):
        if tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Comment:
            if tokens[i][0] == pygments.token.String.Doc: 
                print("YESSSSS")
                print(tokens[i])
            result.append(tokens[i][1])
        else:
            continue
            #tuples in result-(each element e.g 'def', its position in original code file, position in cleaned up code/text) 
            # count2 += len(tokens[i][1])
        # count1 += len(tokens[i][1])
    
    print(result)
    return result


def cleanUp(commentsListFromTokenizer):
    result = " ".join(commentsListFromTokenizer)
    return result


def copyrightsExtraction(comments):
    regexToExtractingCopyRightSt = r'copyright\s+\(?c?\)?[^=^\n].*'
    match = re.findall(regexToExtractingCopyRightSt,comments,re.I|re.M)
    # pattern = re.compile(regexToExtractingCopyRightSt, re.I|re.M)
    # match = pattern.findall(comments)

    return match


def extractDates(extractedCopyrightStatements):
    # print(extractedCopyrightStatements)
    result = []
    # for i in extractedCopyrightStatements:
        # try:
    regexToExtractDates = '\s\d{4}-?(\d{4})?(\s,)?'
    pattern = re.compile(regexToExtractDates, re.I|re.M)
    match = pattern.finditer(extractedCopyrightStatements)
    # print(match)
    # result.append(match)
        # except:
            # continue
    # print(match)
    return match


def extractSpans(iterator, extractedCopyrightStatements):
    # print(iterator)
    spans = []
    dates = []
    for match in iterator:
        # print(match.span())
        spans.append(match.span())
        # index = match.span() 
        # dates.append(extractedCopyrightStatements[index[0]:index[1]])
    
    return spans

def locateDates(spans,extractedCopyrightStatements):
    # index = spans.span() 
    dates = []
    for i in spans:
        dates.append(extractedCopyrightStatements[i[0]:i[1]])
    return dates

# comments = tokenize(r"D:\2022\Python Practice\regex.py")


def initiator(filePath):
    tokenized = tokenizer(filePath)
    cleanedCode = cleanUp(tokenized)
    # print(cleanedCode)
    copyrights = copyrightsExtraction(cleanedCode)
    print("-----------------------------Copyright Statements in the code file--------------------")
    print(copyrights)
    copyrights = " ".join(copyrights)
    # print(copyrights)
    # unCleanedDates = list(map(extractDates, copyrights))
    unCleanedDates = extractDates(copyrights)
    # unCleanedDates = extractDates(copyrights)
    # print(unCleanedDates.span())
    # print(unCleanedDates)
    # for i in unCleanedDates:
    #     print(i.span())
    # print(unCleanedDates)
    spans = extractSpans(unCleanedDates,copyrights)
    # print(spans)
    dates = locateDates(spans,copyrights)
    print(dates)

    # return copyrights , dates







print(initiator(r"D:\2022\Python Practice\tests.py"))
# with open(r'D:\2022\Python Practice\test2.py', 'r' ,encoding='utf-8' , errors='ignore') as f:
#     text = f.read()


# from comment_parser import comment_parser
# import magic
# # Returns a list of comment_parser.parsers.common.Comments
# print(comment_parser.extract_comments(r"D:\2022\Python Practice\tests.py"))