# Copyright (C) 2022 by SeQuenX  - All Rights Reserved
# This file is part of the ComplyVantage product development,
# and is released under the "Commercial License Agreement".

# You should have received a copy of the Commercial License Agreement license with
# this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com



import re 


text = '''

Copyright (C) 2022 by SeQuenX  - All Rights Reserved
This file is part of the ComplyVantage product development,
and is released under the "Commercial License Agreement".

You should have received a copy of the Commercial License Agreement license with
this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com





'''



CopyrightTexts = '''
Copyright (c) 2010 Daniel Wachsstock

Copyright (C) 2011-2019 Twitter, Inc.

Copyright (C) 2013-2015 The Bootstrap Tour community

Copyright (C) Zeno Rocha

Copyright (C) 2014 Wang Shenwei

(C) Zeno Rocha

Copyright (C) 2018 David DeSandro

Copyright (C) 2013-2015 by Andrea Giammarchi - @WebReflection

Copyright (C) 2014 Yehuda Katz, Tom Dale, Stefan Penner and contributors

Copyright (C) 2018 David DeSandro

Copyright (C) 2020 Jan van der Pas

Copyright (C) 2018 David DeSandro <http://desandro.com>

Copyright © 2021 Zeno Rocha <hi@zenorocha.com>

Copyright (C) 2012 Barnesandnoble.com, llc, Donavon West, Domenic Denicola, Brian Cavalier

Copyright (C) 2011 Tapmodo Interactive LLC, http://github.com/tapmodo/Jcrop

Copyright jQuery Foundation and other contributors, https://jquery.org

Copyright 2012 jQuery Foundation and other contributors, http://jquery.com

Copyright (C) 2014 Jochen Ulrich (http://github.com/j-ulrich/jquery-simulate-ext)

Copyright OpenJS Foundation and other contributors <https://openjsf.org/>

Copyright 2013 by Erik Krogh Kristensen (webbies.dk)

Copyright (C) 2016-2019 David Heinemeier Hansson, Basecamp

Copyright (c) 2019, Sentry

Copyright (c) 2014, Paul Macek

Copyright 2013 Anthon Pang

print("#############################################")
print(re.findall("Copyright.*",text))
print(re.findall(r'Copyright.*',CopyrightTexts , re.I))


'''


CopyrightTexts2 = '''

Author: Oleg Korsunsky <wd@dizaina.net>

Owner: Ben Kamens (http://bjk5.com/)

Author, Email: dave@fontawesome.io, Twitter: http://twitter.com/davegandy, GitHub: https://github.com/davegandy

Author: Andrew Rowls Community (https://github.com/eternicode/bootstrap-datepicker...)

'''
# print(re.findall(text,"Copyright"))
x=None
s = "Welcome to GeeksForGeeks"
regex = r"([a-zA-Z]+) (\d+)"
 
match = re.search(regex, "I was born on June 24")
 
if match != None:
 
    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.
 
    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print ("Match at index %s, %s" % (match.start(), match.end()))
 
    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)
 
    # So this will print "June 24"
    print ("Full match: %s" % (match.group(0)))
 
    # So this will print "June"
    print ("Month: %s" % (match.group(1)))
 
    # So this will print "24"
    print ("Day: %s" % (match.group(2)))
 
else:
    print ("The regex pattern does not match.")
# here x is the match object
res = re.search(r"{Copyright}",s  , flags=re.IGNORECASE)
print(res)
# print(res.re)
# print(res.string)
def stringMatching(text):
    if text==None:
        return None
    ot = re.findall(r'CopyRight',text)
    ot = re.findall(r'CopyRight([\s\S]',text)
    ot = re.findall(r'CopyRight([\s\S]*',text)
    ot = re.findall(r'CopyRight([\s\S]*[\n]',text)
    ot = re.findall(r'CopyRight([\s\S]*[\n][\n|\r]',text)
    ot = re.findall(r'CopyRight([\s\S]*[\n][\n|\r\n]',text)
    ot = re.findall(r'CopyRight([\s\S]*[\n][\n|\r\n|\r]',text)
    return re.findall(r'Copyright ([\s\S]*)[\n|\r\n|\r]',text)
stringMatching(x)


print("------------------COPYRIGHT TEXT--------------------")
print(re.findall(r'Copyright ([\s\S\w]*)[\n|\r\n|\r][\n]',CopyrightTexts))

# pattern = re.compile("hello", flags=re.I)

# pattern = re.compile("hello")
# match = pattern.match("hello world")
# print(match)
# print(match.span())
# print(match.start())
# print(match.end())
# # pattern = re.compile("hello")
# # print(pattern)
# # from utils import highlight_regex_matches
# # highlight_regex_matches(pattern, "say hello hello")
# pattern.findall("say hello hello")
# re.search(re.escape("C:\Windows\System32"), txt)
# matches = pattern.finditer("say hello hello")
# for match in matches:
#     print(match.span())
# (4, 9)
# (10, 15)

print("#############################################")
print(re.findall("Copyright.*",text))

print("ALL Copyrights")
print(re.findall(r"Copyright.*",CopyrightTexts , re.I))
# s = '<html><head><title>Title</title>'

# print(re.findall('a{1,2}', 'aaaa a aa'))










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



print("######################COPY RIGHTTTTTT########################")

print(clean_copyright(text))



'''
This regex is not extracting the "copyright 2014 Daniel", copyright statements 
but it is extracting the 

'''
regexForMultipleCR = '[cC]opyright\s+\(?[cC]+\)?[^=^\n.]*'

regexForMultipleCR = '[cC]opyright\s+(\d{4,})?\(?[cC]*\)?[^=^\n.]*'

regexForMultipleCR = '[cC]opyright\s+(\d{4,})?\(?[cC]*\)?[^=^\n.]*'

cp2 = '''
Copyright (c) 2010 Daniel Wachsstock

Copyright (C) 2012 Barnesandnoble.com, llc, Donavon West, Domenic Denicola, Brian Cavalier

Copyright (C) 2014 Jochen Ulrich (http://github.com/j-ulrich/jquery-simulate-ext)

Copyright OpenJS Foundation and other contributors <https://openjsf.org/>

Copyright OpenJS Foundation and other contributors <https://openjsf.org/>

Copyright (c) 2014, Paul Macek

Copyright (C) 2011-2019 Twitter, Inc.

Copyright (C) 2013-2015 The Bootstrap Tour community

Copyright (C) Zeno Rocha

Copyright (C) 2014 Wang Shen

Copyright 2014 Daniel

Copyright = 5

def copyright(num):

class copyright:

def copyright(c): 

copyright=5

copyright = 8 

def copyright(Num):
'''

regexFinalForAllCopyrights = r'^copyright\s+\(?c?\)?[^=^\n].*'
ot = r"^[cC]opyright\s+([cC])?[^=^\n].*"
print(ot)
print("-----------------------------ALL COPYRIGHTS-------------------------------------")
copyrightStatements = re.findall(ot,cp2,re.I|re.M)
print(copyrightStatements.group())
print(copyrightStatements)
print("Length of Copyright Statement: ",len(copyrightStatements))


extractdates = '\s\d{4}-?(\d{4})?(\s,)?'
print(extractdates)
copyrightStatements = re.findall(extractdates,cp2,re.I|re.M)
# print("Dates: ", copyrightStatements)
pattern = re.compile(extractdates)
replace = pattern.sub("NONEEEEEEEEEEEEE", cp2, re.I|re.M)
print("replace" , replace)