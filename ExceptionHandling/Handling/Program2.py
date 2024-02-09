print('Start Code')


try:
    num1 = int(input())
    num2 = int(input())
except:
    print('ValueError Exception Handled')

#if we enter a String it will throw a Value error Exception which can be caught by us 
try:
    print(num1+num2)

except:
    print('name Error has be handled here')
print('End Code')

