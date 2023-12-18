from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text()+','


print(data_raw)

sum=0
hash=0
for char in data_raw:
    print(char)

    if(char==','):
        print(hash)
        print('reset')
        
        sum+=hash
        hash=0
        continue

    hash+=ord(char)
    hash=hash*17
    hash=hash%256
    

print(sum) 
