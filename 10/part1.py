from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
acosMap = [list(line) for line in data_raw]
#find S coor
for y in range(len(acosMap)):
    for x in range(len(acosMap[y])):
        if(acosMap[y][x]=='S'):
            Spos=[y,x]
            break
keys2={
    '|':[(-1,0),(1, 0)],
    '-':[(0, -1),(0, 1)],
    'L':[(-1,0),(0, 1)],
    'J':[(-1,0),(0, -1)],
    '7':[(0, -1), (1, 0)],
    'F':[(0, 1), (1, 0)   ],
    '.':[( 0, 0), ( 0, 0)  ],
    'S':[ (-1,0),(0, 1),  (1, 0),(0, -1) ]
}
'''
       (-1,0)
(0, -1)  []  (0, 1)
       (1, 0)

COLOUMN FIRST THEN ROW       
'''
startingBox=startingBox=keys2['S']
currCoor=Spos
count=0
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
            for entry in keys2[charr]:
                if([checkCharY+entry[0],checkCharX+entry[1]]==currCoor):
                    startingBox=[(-1,0),(1,0),(0,-1),(0,1)]
                    startingBox=keys2[charr].copy()
                    startingBox.remove(entry)
                    found=True
                    currCoor=[checkCharY,checkCharX]
        if found:
            break
    count+=1
    if(currCoor==Spos):
        break     
print(count//2)  