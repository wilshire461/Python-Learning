#This Function solves the diophantine equation for a tuple of values ordered least to greatest.
def numNuggets(packages,nuggets):
    for large in range(0,nuggets/packages[2]+1):
        #Maximum range takes into account currently selected larger pack
        for medium in range(0,((nuggets-large*packages[2])/packages[1])+1):
            small=(nuggets-packages[2]*large-packages[1]*medium)/packages[0]
            totNuggets = packages[2]*large+packages[1]*medium + packages[0] * small
            #Return True when we find the first soltion
            if nuggets == totNuggets:
                return True
    #When all combinations have been iterated without a solution return false
    return False               

#state varables
n=0
unsolvable=[]
numSolved=0
packsize = (3,7,11)
#Keeps Solving diophantine equations until we have solved at least as many in a row as the smallest pack
while numSolved <= packsize[0]:
    noSolution=False
    n+=1
    #break if no solution found before 200
    if n >= 200:
        noSolution = True
        break
    solved = numNuggets(packsize,n)
    if solved == True:
        numSolved+=1

    if solved == False:
        numSolved=0
        unsolvable.append(n)    
if noSolution == False:
    print "Given package sizes %i, %i and %i the largest number of McNuggets that cannot be bought in exact quantity is: %i" % (packsize[0],packsize[1],packsize[2],unsolvable.pop())
else:
    print "Can not find a solution less than 200"       

#Some results from the code
#8,9,20=39
#7,18,23=52
#3,7,11=8