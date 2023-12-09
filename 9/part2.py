from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
sum=0
for history in data_raw:
    history = [int(x) for x in history.split()]
    sequence=[]
    seqCount=0
    sequence.append(history)
    while(not all(x == 0 for x in sequence[seqCount]) ):
        sequence.append([])
        seqCount+=1
        for i in range(len(sequence[seqCount-1])-1):
            sequence[seqCount].append(sequence[seqCount-1][i+1]-sequence[seqCount-1][i])
    add=0
    for i in range(len(sequence)-1,-1,-1):
        add=sequence[i][0]-add
    sum+=add
print(sum)