from pathlib import Path
data_raw = Path(__file__).with_name("input_test_p2.txt").read_text().splitlines()
acosMap = [list(line) for line in data_raw]
#find S coor
for y in range(len(acosMap)):
    for x in range(len(acosMap[y])):
        if(acosMap[y][x]=='S'):
            Spos=[y,x]
            break
validDirections={
    '|':[(-1,0),(1, 0)],
    '-':[(0,-1),(0, 1)],
    'L':[(-1,0),(0, 1)],
    'J':[(-1,0),(0,-1)],
    '7':[(0,-1),(1, 0)],
    'F':[(0, 1),(1, 0)],
    '.':[(0, 0),(0, 0)],
    'S':[(-1,0),(0, 1),(1, 0),(0, -1)]
}
'''    (-1,0)
(0, -1)  []  (0, 1)
       (1, 0)     
'''
startingBox=startingBox=validDirections['S']
currCoor=Spos
count=0
path=[]
pathCoor=[]
while(True):
    #check adj nodes that are valid for current node
    for boxY,boxX in startingBox:
        found=False
        checkCharX=currCoor[1]+boxX
        checkCharY=currCoor[0]+boxY
        #check if node is on map
        if(0<=checkCharY<len(acosMap) and 0<=checkCharX<len(acosMap[0])): 
            charr = acosMap[checkCharY][checkCharX]
            #check if a adj node connects to currnode 
            for entry in validDirections[charr]:
                if([checkCharY+entry[0],checkCharX+entry[1]]==currCoor):
                    startingBox=validDirections[charr].copy()
                    startingBox.remove(entry)
                    found=True
                    
                    currCoor=[checkCharY,checkCharX]
                    pathCoor.append(currCoor)
                    path.append(charr)
        if found:
            break
    count+=1
    if(currCoor==Spos):
        break     
print(count//2)  

for y in range(len(acosMap)):
    for x in range(len(acosMap[y])):
        print(acosMap[y][x]+'  ',end='')
    print()

print(path)
print(pathCoor)

blankMap= [['.' for _ in range(len(acosMap[0])*3)] for _ in range(len(acosMap)*3)]

for y in range(len(blankMap)):
    for x in range(len(blankMap[y])):
        print(blankMap[y][x]+'  ',end='')
    print()
print()
for i in range(len(path)):
    r=pathCoor[i][1]
    c=pathCoor[i][0]

    if path[i]=='|':
      blankMap[3*c+0][3*r+1] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+2][3*r+1] = 'x'
      
    elif path[i]=='-':
      blankMap[3*c+1][3*r+0] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+1][3*r+2] = 'x'
    elif path[i]=='7':
      blankMap[3*c+1][3*r+0] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+2][3*r+1] = 'x'
    elif path[i]=='F':
      blankMap[3*c+2][3*r+1] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+1][3*r+2] = 'x'
    elif path[i]=='J':
      blankMap[3*c+0][3*r+1] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+1][3*r+0] = 'x'
    elif path[i]=='L':
      blankMap[3*c+0][3*r+1] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+1][3*r+2] = 'x'
    elif path[i]=='S':
      blankMap[3*c+0][3*r+1] = 'x'
      blankMap[3*c+1][3*r+1] = 'x'
      blankMap[3*c+1][3*r+2] = 'x'
      blankMap[3*c+1][3*r+0] = 'x'
      blankMap[3*c+2][3*r+1] = 'x'


for y in range(len(blankMap)):
    for x in range(len(blankMap[y])):
        print(blankMap[y][x]+'  ',end='')
    print()

