
def isSymbol(s):
    return not s.isnumeric() and s!='.' and s!='\n'

from collections import defaultdict 
sum=0
file = open('input.txt','r')
lines = file.readlines()
nums=defaultdict(list)
gears=set()
for col in range(len(lines)):

    numFound=False
    buildNum=''
    valid=False
    gearing=[0,0]

    for row in range(len(lines[col])):
        #print(lines[col][row])
        if(not lines[col][row].isnumeric() and numFound):
            
            if valid==True:
                #print(buildNum)
                sum+=int(buildNum)

                for gear in gears:
                    nums[gear].append(int(buildNum))
                gears = set() 

            
                gearing=[0,0]
            valid=False
            numFound=False
            buildNum=''

        if(lines[col][row].isnumeric()):

            for windowC in [-1,0,1]:
                for windowR in [-1,0,1]:
                    if(0<=col+windowC <len(lines) and 0<=row+windowR <len(lines[col])):
                      
                        if(isSymbol(lines[col+windowC][row+windowR])):
                            valid=True

                        #PART2
                        if(lines[col+windowC][row+windowR]=='*'):
                            valid=True
                            gearing=[col+windowC,row+windowR]
                            gears.add((col+windowC,row+windowR))

                      

                            


                        
            numFound=True
            buildNum+=lines[col][row]
print(sum)
p2=0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)


