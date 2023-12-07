
file=open('input.txt','r')
filelines=file.readlines()
file.close()
seeds=[int(x) for x in filelines[0].split(':')[1].strip().split()]
index=3
filelines.append('\n')
sour2des=[[] for x in range(7)]
for i in range(7):
    while(filelines[index]!='\n'):
        sour2des[i].append([int(x) for x in filelines[index].split()])
        index+=1
    index+=2
answertable=[0]*8
locations=[]


print(seeds)

for seed in seeds:
    answer=seed
    answertable[0]=answer
    for x in range(7):
        found=False
        for i in range (len(sour2des[x])):
            if(sour2des[x][i][1]<=answer<=sour2des[x][i][1]+sour2des[x][i][2]):
                answer=sour2des[x][i][0]-sour2des[x][i][1]+answer
                break
        answertable[x+1]=answer
    locations.append(answertable[7])
    print (answertable)
print(min(locations))