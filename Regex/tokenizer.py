
import pygments
import pygments.token
import pygments.lexers

def tokenizer(filePath):

    print(filePath)
    with open(filePath, 'r' ,encoding='utf-8' , errors='ignore') as f:
        text = f.read()
    lexer = pygments.lexers.guess_lexer_for_filename(filePath, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    for i in range(lenT):
        if tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Comment:
            # if tokens[i][0] in pygments.token.literal.String.Doc: 
            #     print("YESSSSS")
            #     print(tokens[i])
            result.append(tokens[i][1])
        else:
            continue
    return result