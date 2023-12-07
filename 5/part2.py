
file=open('input_given.txt','r')
filelines=file.readlines()
file.close()
seeds=[int(x) for x in filelines[0].split(':')[1].strip().split()]
print(seeds)
index=3
filelines.append('\n')
sour2des=[[] for x in range(7)]
for i in range(7):
    while(filelines[index]!='\n'):
        sour2des[i].append([int(x) for x in filelines[index].split()])
        index+=1
    index+=2

answertable=[0]*8
locationd=0
index=1
for seedindex in range(0,len(seeds),2):
    print('On seed: ' +str(seedindex+1))
    starting=seeds[seedindex]
    rangeseed=seeds[seedindex+1]
    seed=starting
    while(seed<starting+rangeseed):
        answer=seed
        answertable[0]=answer
        for x in range(7):
            found=False
            for i in range (len(sour2des[x])):
                if(sour2des[x][i][1]<=answer<=sour2des[x][i][1]+sour2des[x][i][2]):
                    answer=sour2des[x][i][0]-sour2des[x][i][1]+answer
                    break
            answertable[x+1]=answer
        if(answertable[7]<locationd or seed==seeds[0]):
            locationd=answertable[7]
            print(locationd)
   
        seed+=1
    
print(locationd)
