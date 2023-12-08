from pathlib import Path
data_raw = Path(__file__).with_name("input_given.txt").read_text().splitlines()
hands=[]
bets=[]
#get data
for i in range(len(data_raw)):
    hands.append(data_raw[i].split(' ')[0])
    bets.append(int(data_raw[i].split(' ')[1]))
scores=[]
#for each hand

for x in range(len(hands)):
    bet=bets[x]
    hand=hands[x]
    count={}
    
    for i in range(5):
        if(hand[i] not in count):
            count[hand[i]]=0
        count[hand[i]]+=1

    #if J is found, store # Js and  delete
    jcount=0
    if('J' in count):
        jcount=count['J']
        del count['J']

    count=sorted(count.values(), reverse=True)

    #2 cases: 5 Js= 5 of a kind, <5 Js= best possible way to get rank is it add J to most # cards
    if(jcount==5):
        count=[5]
    else:
        count[0]+=jcount
   
    
    #get numaeric value of each card, append, lower int= lower priority
    for i in range(5):
        count.append('J23456789TJQKA'.index(hand[i]))

    if(jcount==4):
        print([count,bet])
    scores.append([count,bet])

#sort answers
scores.sort()
factor = 1
total = 0
for g in scores:
    bid = g[1]
    total += factor * bid
    factor += 1
print(total)