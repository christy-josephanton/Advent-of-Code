sum=0
file = open('input.txt','r')
lineP='.'*140+'\n'
lineC='.'*140+'\n'

def isSymbol(s):
    return not s.isnumeric() and s!='.' and s!='\n'

lines = file.readlines()
lines[len(lines)-1]+='\n'
lines.append('.'*140+'\n')

for x in range(len(lines)):
    lineN=lines[x]

    numFound=False
    buildNum=''
    valid=False
    prevValid=False
    nextValid=False

    for i in range(len(lineC)):

        if(lineC[i]!='\n' ):
            nextValid=isSymbol(lineP[i+1]) or isSymbol(lineC[i+1]) or isSymbol(lineN[i+1])

        if(not lineC[i].isnumeric() and numFound):
            if(valid): sum+=int(buildNum)
            valid=False
            numFound=False
            buildNum=''

        if(lineC[i].isnumeric()):
            
            if(isSymbol(lineP[i])or isSymbol(lineN[i]) or prevValid or nextValid):
                valid=True

            numFound=True
            buildNum+=lineC[i]
        
        #check if symbol is adj in prev
        prevValid=isSymbol(lineP[i]) or isSymbol(lineC[i]) or isSymbol(lineN[i])
    lineP=lineC
    lineC=lineN

print(sum)