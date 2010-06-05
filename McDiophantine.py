def numNuggets(nuggets):
    for numPack20 in range(0,nuggets/20+1):
        #When setting to range it takes into account the currently selected pack of 20
        for numPack9 in range(0,((nuggets-numPack20*20)/9)+1):
            numPack6=(nuggets-20*numPack20-9*numPack9)/6
            totNuggets = 20*numPack20+9*numPack9 + 6 * numPack6
            if nuggets == totNuggets:
                return True
    return False               

#state variables
n=0
unsolvable=[]
numSolved=0
#Keep solving until 5 are solved in a row
while numSolved <= 5:
    n+=1
    solved = numNuggets(n)
    if solved == True:
        numSolved+=1

    if solved == False:
        numSolved=0
        unsolvable.append(n)

print 'Largest number of McNuggets that cannot be bought in exact quantity: %i' % unsolvable.pop()




