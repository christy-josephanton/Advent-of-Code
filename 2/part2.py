sum=0
file = open('input.txt','r')
for game in file:
    game=game.replace(",","").strip().split(':')[1].split(';')
    for i in range(len(game)): game[i]=game[i].split(' ')
    Rcount, Gcount, Bcount = 0, 0, 0
    for line in game:
        for i in range(len(line)-1,0,-2):
            if(line[i]=='red'): Rcount=max(int(line[i-1]),Rcount)
            if(line[i]=='green'): Gcount=max(int(line[i-1]),Gcount)
            if(line[i]=='blue'): Bcount=max(int(line[i-1]),Bcount)
    sum+=Rcount*Gcount*Bcount
print(sum)