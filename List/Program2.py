numlist = [num for num in range(1,11)]

print(numlist)
print(type(numlist))

numlist = [num*num for num in range(1,11)]
print(numlist)
print(type(numlist))

numlist = [num*num for num in range(1,11) if num%2 == 1]
print(numlist)
print(type(numlist))

evenlist = list()
for num in range(1,11):
    if num%2 ==0:
        evenlist.append(num*num)
print(evenlist)
print(type(evenlist))
