team = ['virat','rohit','shreyash','klRahul']

player = input("Enter the player to : ")

for i in team:
    if(i == player):
        print("%s is in a team"%i)
        break;
    
else:
    print("%s is not in a team"%player)

    # this is else suite and it will automatically detect no else after the loop no need to use flag 
