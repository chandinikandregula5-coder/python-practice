'''
REGULAR EXPRESSIONS or REGEX
----------------------------
regex is a squence of char that from a searching pattern...
this can be used to check if a string contain the specified search pattern

---->python has a built-in package called 're'which can be used to work with RegEX....

Functions in re
---------------
1.Fimdall
2.search
3.fullmatch

metachar
--------
[]-->a-z,A-Z,0-9 and any specified sequence....
.-->here each dot is one char
^--->this look for the,string is starting with specified sequence or not...
$--->this look for the 
import re
any_="c is a foundational,general-purpose programming language"
print(re.findall('[als]',any_))

import re
any_="c is a foundational,general-purpose programming language"
print(re.findall('pu...e',any_))

import re
any_="c is a foundational,general-purpose programming language"
print(re.findall('pr...r.g',any))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('^python is',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('age$',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('pro.*gramming',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('pro.?gramming',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('pro.+gramming',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('p.{7}',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('\s',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('\S',any_))

import re
any_ = "c is a foundational,general-purpose2 programming3 language"
print(re.findall('\d',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('\W',any_))

import re
any_ = "c is a foundational,general-purpose programming language"
print(re.findall('w',any_))

special sequence
\S=NO Space
\s=only spaces
\d=only digits
\w=matches any word char
\W=returns non words
'''
import re
mobile_=input("enter 10 digit mobile num")
how= re.fullmatch('[6-9][0-9]{9}',mobile_)
if how:
    print(f"{mobile_} this is india number")
else:
    print(f"{mobile_}this is not indian number")














