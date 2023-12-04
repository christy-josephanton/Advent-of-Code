file = open('input.txt','r')
sum=0
for line in file:
    first = next(char for char in line if char.isnumeric())
    second = next(char for char in reversed(line) if char.isnumeric())
    sum+=int(first+second)
print(sum) 
#52974 PART 1
#52638 PART 2 WRONG
#53340 PART 2 RIGHT