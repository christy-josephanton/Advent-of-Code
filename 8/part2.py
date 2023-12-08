from pathlib import Path
from math import gcd
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
path=data_raw[0]
dmap={}
for line in data_raw[2:]:
    node = line.split(' =')[0]
    left = line.split(' =')[1].replace(' (','').replace(')','').split(', ')[0]
    right= line.split(' =')[1].replace(' (','').replace(')','').split(', ')[1]
    dmap[node]=[left,right]

endwA=[]
for x in dmap:
    if x[2]=='A':
        endwA.append(x)
print(endwA)
i=0
count2Z={}
count=0
while True:
    step= 0 if path[i] =='L' else 1
    #iff Z found, keep track of count
    for j in range(len(endwA)):
        if(endwA[j][2]=='Z'):
            count2Z[j]=count
    #move to next node
    for x in range(len(endwA)):
        endwA[x]=dmap[endwA[x]][step]
    #exit if all Z nodes ofund
    if len(count2Z)==len(endwA): break
    #increment path index
    i = 0 if i==len(path)-1 else i+1
    count+=1
print(count2Z)
lcm = 1
for i in count2Z.values():
    lcm = lcm*i//gcd(lcm, i)
print(lcm)