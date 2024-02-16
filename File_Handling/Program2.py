# wirte mode if the file is not present it will create a new file 
# and in w mode the writing starts from zeroth index it will erase all 
# data first and then start to write

fileObj = open('new.txt','w')
fileObj.write('hello\nthis\nis\nok')
