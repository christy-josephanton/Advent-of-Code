from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text()+','
sum=0
hash=0
for char in data_raw:
    if char==',':
        sum+=hash
        hash=0
        continue
    hash+=ord(char)
    hash=hash*17%256
print(sum)