file=open('input.txt','r')
times=[int(next(file).strip().split(':')[1].replace(' ',''))]
distances=[int(next(file).strip().split(':')[1].replace(' ',''))]
file.close()
prod=1
for i in range(len(times)):
    PointR=0
    PointL=times[i]
    finishR=True
    finishL=True
    while(finishR and finishL):
        if(finishR):
            if(PointR*(times[i]-PointR)>distances[i]):
                finishR=False
            else:
                PointR+=1
        if(finishL):
            if(PointL*(times[i]-PointL)>distances[i]):
                finishL=False
            else:
                PointL-=1
    prod*=PointL-PointR+1
print(prod)