import re

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
extractdates = '\s\d{4}-?(\d{4})?(\s,)?'

# match = re.findall(regexFinalForAllCopyrights,cp2,re.I|re.M)
# print(match)


dateMatch = ["".join(x) for x in re.findall(extractdates, extractdates)]
print(dateMatch)