# append 
# extend
# index

player = ['Rohit','Shubman','Virat','Shreyash','KlRahul']

print(player)

player.extend(['Jaddu','Shammi','Bumrah'])
print(player)

# insert

player.insert(5,'SKY')
print(player)

# remove

player.remove('Jaddu')
print(player)

# pop removes and return the item at index from a list

player.pop() # pop the last item in the list
print(player)

# clear     removes all elements from the list 

player.clear()
print(player)

# count     counts the no of times the element is present in the list

player = ['Rohit','Shubman','Virat','Shreyash','KlRahul']
print(player.count('Shreyash'))

# index returns the index of first occurance of the element in the list

print(player.index('Shubman'))

# reverse   Reverses a list 'In Place'

player.reverse()
print(player)

# sort  it will sort the list in ascending order and return none

batsmen = player.copy()
print(player)
print(batsmen)
