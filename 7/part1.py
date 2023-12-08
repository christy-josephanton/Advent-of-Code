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
    #count number of each card
    for i in range(5):
        if(hand[i] not in count):
            count[hand[i]]=0
        count[hand[i]]+=1
    #sort large to small, append to list
    count=sorted(count.values(), reverse=True)
    #get numaeric value of each card, append, lower int= lower priority
    for i in range(5):
        count.append('23456789TJQKA'.index(hand[i]))
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