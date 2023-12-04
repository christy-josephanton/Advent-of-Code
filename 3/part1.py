sum=0
file = open('input.txt','r')
lineP='.'*141
lineC='.'*140


def isSymbol(s):

    if not s.isnumeric() and s!='.' and s!='\n':
        return True


    return False
    

for lineN in file:
  
    lineC=lineN
    lineC='.1.61........397...#386...=........313........-...&............*......*................@.............../.........621+....................169\n'
    lineN='.../..........*574.587..*........1/1......904.......412.........*.................*.................................=.....637.%......*..../.\n'

    print(lineP)
    print(lineC)
    print(lineN)

    #print(lineN)
    numFound=False
    buildNum=''
    valid=False
    prevValid=False

    for i in range(len(lineC)):
    
        lineP[i]
        lineC[i]
        lineN[i]

        #TODO add checking for adj in next columns


        if(not lineC[i].isnumeric() and numFound):
            
    
            print('Checking Number: '+str(buildNum))
            #check if valid
            if(valid):
                print('Valid!')
                sum+=int(buildNum)
            valid=False

            
            numFound=False
            buildNum=''


        if(lineC[i].isnumeric()):
            
            if(isSymbol(lineP[i]) or isSymbol(lineN[i]) or isSymbol(lineP[i]) or isSymbol(lineN[i]) or prevValid):
                valid=True

            numFound=True
            buildNum+=lineC[i]
        
        #check if symbol is adj in prev
        prevValid=isSymbol(lineP[i]) or isSymbol(lineC[i]) or isSymbol(lineN[i])
            

    break

    #move on to next line
    lineP=lineC
    lineC=lineN