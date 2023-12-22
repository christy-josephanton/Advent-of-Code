from collections import deque
from pathlib import Path
data_raw = Path(__file__).with_name("input_test.txt").read_text().splitlines()
grid = [list(line) for line in data_raw]

for l in grid:
    print(l)



startingPos=[]
for i in range(len(grid)):
    startingPos.append(((i,-1,0,1)))
    startingPos.append(((i,len(grid[0]),0,-1)))
for j in range(len(grid[0])):
    startingPos.append(((-1,j,1,0)))
    startingPos.append(((i,len(grid),-1,0)))



seen = set()
#start position: 0,-1, direction: 0,1
q = deque([(0,-1,0,1)])
while q:
    i, j, di, dj = q.pop()

    ii, jj = i + di, j + dj
    if (ii, jj, di, dj) in seen: continue
    if not (0 <= ii < len(grid) and 0 <= jj < len(grid[0])): continue

    seen.add((ii, jj, di, dj))

    tile = grid[ii][jj]

    match tile:
        case "/":
            di, dj = -dj, -di
        case "\\":
            di, dj = dj, di
        case "|":
            if dj:
                di, dj = 1, 0
                q.append((ii, jj, -1, 0))
        case "-":
            if di:
                di, dj = 0, 1
                q.append((ii, jj, 0, -1))
    q.append((ii, jj, di, dj))
energized = {x[:2] for x in seen}
print(len(seen))
print(len(energized))
len(energized)




print(startingPos)