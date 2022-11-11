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

s = "Welcome to GeeksForGeeks"
 
# here x is the match object
# res = re.search(r"{to}",s  , flags=re.IGNORECASE)
# print(res)
# # print(res.re)
# print(res.string)

output = re.findall(r'Copyright ([\s\S]*)[\n|\r\n|\r]',text, re.IGNORECASE)
print(output)