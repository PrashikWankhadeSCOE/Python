"""
continue statement is same as pass statement but 
it will not print anything below it 
it will simlpy skip that loop 

where as if we use break it break the loop
which means the loop will not flow after that 
but by using conting that iteration will stop there where as next will continue

and if we use pass it will pass the if or else if or else statement 
but will run the prigram from nextline after the if else condition

"""

for i in range(1,10):
    if(i%2==0):
        continue;
    else:
        print('Not in countinue ')
