from collections import defaultdict
from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().split(',')

hash=0
boxes = defaultdict(dict)
for ind in range(len(data_raw)):
    hash=0
    for chari in range(len(data_raw[ind])):
        char=data_raw[ind][chari]
        if (char=='='):
            boxes[hash][data_raw[ind][:chari]]=int(data_raw[ind][chari+1])
            break
        if(char == '-'):
            boxes[hash].pop(data_raw[ind][:chari],None)
            break
        hash+=ord(char)
        hash=hash*17
        hash=hash%256
sum=0
for i in boxes:
    for j,l in enumerate(boxes[i].values()):
        sum+=(i+1)*(j+1)*(l)
print(sum)