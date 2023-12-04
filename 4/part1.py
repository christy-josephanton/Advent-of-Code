file = open('input.txt','r')
sum=0
for line in file:
    winners,card=line.split(':')[1].strip().split('|')
    winners = [int(x) for x in winners.split()]
    card = [int(x) for x in card.split()]
    intersect=len(set(winners)&set(card))
    if(intersect>0): intersect=2**(intersect-1)
    sum+=intersect
print(sum)