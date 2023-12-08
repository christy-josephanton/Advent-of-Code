from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
path=data_raw[0]
dmap={}
for line in data_raw[2:]:
    node = line.split(' =')[0]
    left = line.split(' =')[1].replace(' (','').replace(')','').split(', ')[0]
    right= line.split(' =')[1].replace(' (','').replace(')','').split(', ')[1]
    dmap[node]=[left,right]
count=0
currnode='AAA'
i=0
while True:
    step= 0 if path[i] =='L' else 1
    if currnode=='ZZZ': break
    currnode=dmap[currnode][step]
    i = 0 if i==len(path)-1 else i+1
    count+=1
print( count)