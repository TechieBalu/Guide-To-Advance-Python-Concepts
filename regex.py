# Copyright (C) 2022 by SeQuenX  - All Rights Reserved
# This file is part of the ComplyVantage product development,
# and is released under the "Commercial License Agreement".

# You should have received a copy of the Commercial License Agreement license with
# this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com



import re 


text = '''Copyright (C) 2022 by SeQuenX  - All Rights Reserved
This file is part of the ComplyVantage product development,
and is released under the "Commercial License Agreement".

You should have received a copy of the Commercial License Agreement license with
this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com'''



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
'''


CopyRightTexts2 = '''

Author: Oleg Korsunsky <wd@dizaina.net>

Owner: Ben Kamens (http://bjk5.com/)

Author, Email: dave@fontawesome.io, Twitter: http://twitter.com/davegandy, GitHub: https://github.com/davegandy

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
print(re.findall(r'Copyright ([\s\S]*)[\n|\r\n|\r][\n]',text))