file = open('input.txt','r')
sum=0
nums={"zero":'0o',"one":'o1e',"two":'t2o',"three":'t3e',"four":'f4r',"five":'f5e',"six":'s6x',"seven":'s7n',"eight":'e8t',"nine":'n9e'}
for line in file:
    for key in nums: line = line.replace(key,nums[key])
    first = next(char for char in line if char.isnumeric())
    second = next(char for char in reversed(line) if char.isnumeric())
    sum+=int(first+second)
print(sum) 
#52974 PART 1
#52638 PART 2 WRONG
#53340 PART 2 RIGHT