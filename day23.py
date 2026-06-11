'''
FILE-HANDLING
--> file handler is an object of file to mintain several function of file like,creating,reading,updating and deleting the file..

open a file
-----------
1.open()
2.with open()

modes
-----
'r'--->is used to reading the file,error if file does not exist...

'a'--->is used to add the text into file at last index,if file does not exist...

'w'---->is used to txtx into file but it will override of all txt inside file....

if the file does not exist it will create a new file (no error is thrown)

'x'---->used to create file---but will through error if we are used
'r' mode to create....
method
-------
write()
used for both 'a' and 'w' mode

read()
this method can read entire file chunk by chunk where we can specify the size

readline()
can read only one line at a time in a file...

readlines()
it will read entire file and gives in a list where each line is each index in the list

with open('kanaka.txt','w') as any_:
    any_.write('hello')

any_=open('demo.txt','r')
print(any_.read())
any_.close()


any_=open('demo.txt','r')
print(any_.read(2))
any_.close()
