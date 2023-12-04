from collections import defaultdict
file = open('input.txt','r')
sum=0
sratchcard_instances=defaultdict(int)
count=1
for line in file:
    sratchcard_instances[count]+=1
    winners,card=line.split(':')[1].strip().split('|')
    winners = [int(x) for x in winners.split()]
    card = [int(x) for x in card.split()]
    intersect=len(set(winners)&set(card))

    for i in range(1,intersect+1):
        sratchcard_instances[count+i]+=sratchcard_instances[count]

    if(intersect>0): intersect=2**(intersect-1)
    sum+=sratchcard_instances[count]
    count+=1

print(sum)
