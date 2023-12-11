from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()


acosMap = [list(line) for line in data_raw]

#find S coor
for y in range(len(acosMap)):
    for x in range(len(acosMap[y])):
        if(acosMap[y][x]=='S'):
            Spos=[y,x]
            break

#for line in acosMap:
#    print(line)
#print(Spos)




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


#check all 4 boxes
startingBox=[(-1,0),(1,0),(0,-1),(0,1)]

currchar='S'
currCoor=Spos

count=0

while(True):
    for boxY,boxX in startingBox:
        found=False

        checkCharX=currCoor[1]+boxX
        checkCharY=currCoor[0]+boxY



        if(0<=checkCharY<len(acosMap) and 0<=checkCharX<len(acosMap[0])): #check 4 boxes around it, within grid
            charr = acosMap[checkCharY][checkCharX]




            #print(charr+"  "+str([currCoor[0]+boxY,currCoor[1]+boxX]))
            
            #print(charr)

            #print(keys2[charr])

            for entry in keys2[charr]:
                #print(entry)
                #print([checkCharY+entry[0],checkCharX+entry[1]])
                if([checkCharY+entry[0],checkCharX+entry[1]]==currCoor):
                    #print(True)
                    #print(charr+"  "+str([currCoor[0]+boxY,currCoor[1]+boxX]))
                    startingBox=[(-1,0),(1,0),(0,-1),(0,1)]
                    startingBox=keys2[charr].copy()
                    startingBox.remove(entry)
                    found=True
                    currchar=charr
                    currCoor=[checkCharY,checkCharX]
                    #print(startingBox)
        if found:
            break
        #print()
    count+=1

    #if True:
    if(currchar=='S'):
        break
    
    #print(":::next Node:::")
    #print(currchar+"  " + str(currCoor))
            
print(count//2)

            #print(keys2[charr])



  

   
   
        