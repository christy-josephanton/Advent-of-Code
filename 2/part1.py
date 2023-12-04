sum=0
file = open('input.txt','r')
for game in file:
  
    gameNum=game.split(":")[0].split(" ")[1]
    sum+=int(gameNum)
    game=game.replace(",","").strip().split(':')[1].split(';')
    for i in range(len(game)):
        game[i]=game[i].split(' ')
  
    for line in game:
        Rcount=0
        Gcount=0
        Bcount=0
        for i in range(len(line)-1,0,-2):
            if(line[i]=='red'):
                
                Rcount+=int(line[i-1])
            if(line[i]=='green'):
                
                Gcount+=int(line[i-1])
            if(line[i]=='blue'):
                Bcount+=int(line[i-1])
    
        if(Rcount>12 or Gcount>13 or Bcount>14):
            sum-=int(gameNum)
            break

print(sum)

