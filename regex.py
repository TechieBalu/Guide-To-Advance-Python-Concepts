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