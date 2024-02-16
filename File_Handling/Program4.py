fileobj = open('Incubator.txt','rb')
fileobj.seek(-11,2)

# here 2 represents the end
# -11 represent 11th from end
# to use this 2 and 1 we have to compalsary open out file in binary mode

print(fileobj.read().decode('UTF-8'))
fileobj.seek(-11,1)
# 1 represent from current

print(fileobj.read().decode('utf-8'))


