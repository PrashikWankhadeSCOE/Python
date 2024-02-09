list1 = [10,'Kanha',20,'Rahul',30]

try:
    index = int(input())
    print(list1[index])
    add = list1[0]+list1[3]

except ValueError as err:
    print('Value Error Handled')
except IndexError as err:
    print('Index Error has been Handled')

except TypeError as err:
    print('Type Error Handled')

else:
    print(add)
print('End Code')
