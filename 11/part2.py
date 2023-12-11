from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
data_raw = [list(line) for line in data_raw]

galaxiest=[]
emptyRows=[]
emptyCols=[]
#find all empty rows and cols
for y in range(len(data_raw)):
    empty=True
    for x in range(len(data_raw[y])):
        if(data_raw[y][x]!='.'):  
            empty=False
    if(empty):
        emptyRows.append(y)
for x in range(len(data_raw[0])):
    empty=True
    for y in range(len(data_raw)):
        if(data_raw[y][x]!='.'):
            empty=False
    if(empty):
        emptyCols.append(x)

#find galaxy coors
for y in range(len(data_raw)):
    for x in range(len(data_raw[y])):
        if(data_raw[y][x]!='.'):
            galaxiest.append([y,x])

#find all pairs
pairs = []
for i in range(len(galaxiest)):
    for j in range(i + 1, len(galaxiest)):
        pair = (galaxiest[i], galaxiest[j])
        pairs.append(pair)

#get sum of distances
sum=0
for p1, p2 in pairs:
    #if there is an empty row/col between galazy pair, x 1M or 2 for each empty
    for x in emptyRows:
        if(p1[0]<x<p2[0] or p2[0]<x<p1[0]):
            sum+=999999 #change to 1 for part 1
    for x in emptyCols:
        if(p1[1]<x<p2[1] or p2[1]<x<p1[1]):
            sum+=999999 #change to 1 for part 1
    #add abs range to sum
    sum+=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
print(sum)