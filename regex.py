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

s = "Welcome t00 GeeksForGeeks"
 
# here x is the match object
res = re.search(r"\s+?Copyright",text  , flags=re.IGNORECASE)

# print(res.re)
print(res.string)