# from comment_parser import comment_parser
import pygments
import pygments.token
import pygments.lexers
# f = open(r"D:\2022\Python Practice\regex.py", "r")
# from regex import clean_copyright


def tokenize(filePath ):

    file = open(filePath, "r")
    text = file.read()
    file.close()
    lexer = pygments.lexers.guess_lexer_for_filename(filePath, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    count1 = 0    #tag to store corresponding position of each element in original code file
    count2 = 0    #tag to store position of each element in cleaned up code text
    # these tags are used to mark the plagiarized content in the original code files.
    for i in range(lenT):
        if tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
            result.append(tokens[i][1])
        else:
            continue
            #tuples in result-(each element e.g 'def', its position in original code file, position in cleaned up code/text) 
            # count2 += len(tokens[i][1])
        # count1 += len(tokens[i][1])
    return result



comments = tokenize(r"D:\2022\Python Practice\regex.py")
# print(comments)
# text = " ".join(comments)


# print(text)

# print(clean_copyright(text))

def spaceAndLineBreakRemover(i):
    result = []
    if i == "\n":
        return 
    
    return result
result = []

# print(comments)
for i in comments:
    if i == "\n":
        # print("OK")
        continue
    else: 
        # print("NO")
        result.append(i)
        

# comments = list(map(spaceAndLineBreakRemover,comments))
# print(result)
text = " ".join(result)
# print(text)





import re





end_pats = (r'This implementation just',
            r'Synopsis of public',
            r'The SPU must have',
            r'This is a simple version',
            r'This is a dummy',
            r'stdio_ext\.h',
            r'python script to',
            r'libgen\.h',
            r'Id:.*Exp',
            r'sccs\.',
            r'Tests gleaned',
            r'tar\.h',
            r'tzcalc_limits\.c',
            r'dummy file',
            r'Rearranged for general',
            r'sincos',
            r'POSIX',
            r'Reentrant',
            r'Copied',
            r'These are',
            r'creat',
            r'ARM configuration',
            r'Place holder',
            r'local header',
            r'GNU variant',
            r'default reentrant',
            r'A replacement',
            r'The signgam',
            r'dummy header',
            r'Uniset',
            r'wcsftime\.c',
            r'month_lengths\.c',
            r'Static instance',
            r'Conversion is performed',
            r'Common routine',
            r'l64a')

end_pats_s = (r'FUNCTION',)

end_res = []
for pat in end_pats:
        regex = re.compile(pat, re.I)
        end_res += [regex]

for pat in end_pats_s:
        regex = re.compile(pat)
        end_res += [regex]

left_res = re.compile(r'^[^A-Za-z0-9]*(.*)')
right_res = re.compile(r'(.*)[ /*\t]$')




def clean_copyright(string):
        copyright = []
        have_cpr = False
        cpr_line = re.compile(r'copyright.*(20[0-2][0-9]|19[7-9][0-9])', re.I)
        upper = re.compile(r'[A-Z]')
        lower = re.compile(r'[a-z]')
        modified = re.compile(r'Modified')
        derived = re.compile(r'code is derived from software', re.I)
        skipping = False
        only_upper = False
        for line in string.splitlines():
                m = cpr_line.search(line)
                if m:
                        line = line[m.start():]
                        m = re.match(r'(.*<[^>]+>).*', line)
                        if m:
                                line = line[:m.end()]
                        have_cpr = True

                if not have_cpr:
                        continue

                end = False
                for regex in end_res:
                        if regex.search(line):
                                end = True
                                break
                if end:
                        break

                if modified.search(line):
                        skipping = True
                        continue
                if derived.search(line):
                        skipping = True
                        continue
                if only_upper:
                        if lower.search(line):
                                break
                elif upper.search(line) and not lower.search(line):
                        only_upper = True
                
                line = left_res.match(line).group(1)
                while True:
                        m = right_res.match(line)
                        if not m:
                                break
                        line = m.group(1)
                if skipping:
                        if len(line) == 0:
                                skipping = False
                        continue
                copyright += [line]
        t = '\n'.join(copyright).strip()
        return t







print(clean_copyright(text))