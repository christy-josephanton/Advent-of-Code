from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
data_raw = [list(line) for line in data_raw]
for line in data_raw:
    print(line)


galaxies={}
emptylist=[]

galaxiest=[]
for y in range(len(data_raw)):
    empty=True
    for x in range(len(data_raw[y])):
        if(data_raw[y][x]!='.'):
            galaxies[data_raw[y][x]]=[y,x]
          
            empty=False
    if(empty):
        emptylist.append(y)
for x in reversed(emptylist):
    data_raw.insert(x,['.']*len(data_raw[0]))

emptylist=[]
for x in range(len(data_raw[0])):
    empty=True
    for y in range(len(data_raw)):
        if(data_raw[y][x]!='.'):
            empty=False
    if(empty):
        emptylist.append(x)
for x in reversed(emptylist):
    for i in range(len(data_raw)):
        data_raw[i].insert(x,'.')


for y in range(len(data_raw)):
    for x in range(len(data_raw[y])):
        if(data_raw[y][x]!='.'):
            galaxiest.append([y,x])

print(galaxies)



for line in data_raw:
    print(line)

pairs = []


galaxiesList=galaxiest
for i in range(len(galaxiesList)):
    for j in range(i + 1, len(galaxiesList)):
        pair = (galaxiesList[i], galaxiesList[j])
        pairs.append(pair)

print(len(pairs))
sum=0
for p1, p2 in pairs:
    #print('Distance between: '+str(p1)+' '+str(p2)+' :')
    sum+=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    #print(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))

print(sum)