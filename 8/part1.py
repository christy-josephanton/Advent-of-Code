from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()



path=data_raw[0]

dmap={}
for line in data_raw[2:]:
    node = line.split(' =')[0]
    left = line.split(' =')[1].replace(' (','').replace(')','').split(', ')[0]
    right= line.split(' =')[1].replace(' (','').replace(')','').split(', ')[1]

    #print (node)
    #print(left)
    #print (right)

    dmap[node]=[left,right]




count=0
currnode='AAA'
i=0
while True:

    step=path[i]
    

    if step=='R': step = 1
    else: step=0

   
    currnode=dmap[currnode][step]
    count+=1
    if currnode=='ZZZ':
        break

    if(i==len(path)-1):
        i=0
    else:
        i+=1

print( count)