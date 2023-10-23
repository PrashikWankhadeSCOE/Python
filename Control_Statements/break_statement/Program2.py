playerList = ["Rohit","Virat","Shreyash","KLRahul"]

playerName = input("Enter player name you want to search for : ")

flag = 0
for player in playerList :
    if(player == playerName): 
        print("%s is present in the team "%player)
        flag = flag+1
        break;

if(flag ==0):
    print("%s is not in the team "%playerName)
