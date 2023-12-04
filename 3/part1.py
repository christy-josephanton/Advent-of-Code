
def isSymbol(s):
    return not s.isnumeric() and s!='.' and s!='\n'

sum=0
file = open('input.txt','r')
lines = file.readlines()
for col in range(len(lines)):

    numFound=False
    buildNum=''
    valid=False

    for row in range(len(lines[col])):
        #print(lines[col][row])
        if(not lines[col][row].isnumeric() and numFound):
            
            if valid==True:
                print(buildNum)
                sum+=int(buildNum)
            
            valid=False
            numFound=False
            buildNum=''

        if(lines[col][row].isnumeric()):

            for windowC in [-1,0,1]:
                for windowR in [-1,0,1]:
                    if(0<=col+windowC <len(lines) and 0<=row+windowR <len(lines[col])):
                      
                        if(isSymbol(lines[col+windowC][row+windowR])):
                            valid=True
            numFound=True
            buildNum+=lines[col][row]
print(sum)