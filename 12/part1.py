from pathlib import Path
data_raw = Path(__file__).with_name("input_test.txt").read_text().splitlines()
acosMap = [list(line) for line in data_raw]


def dynamic_spring(DP, sequence, springs):
    return 1



combos=0
for line in data_raw:
    sequence,springs=line.split()
    print(sequence)
    print(springs)
    print()

    DP = {}

    combos+= dynamic_spring(DP,sequence,springs)
    break #remove when want final answer
print (combos)