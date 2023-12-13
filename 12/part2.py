from pathlib import Path
data_raw = Path(__file__).with_name("input.txt").read_text().splitlines()
acosMap = [list(line) for line in data_raw]


def dynamic_spring(DP, sequence, springs):

    if(((sequence, springs)) in DP):
        return DP[(sequence, springs)]
    
    #if there are no springs, still space for numbers -> 0
    # if neither -> 1 , completed
    if not springs:
        if "#" in sequence: return 0
        else: return 1

    #if there are still springs, no space -> no solution
    if not sequence: return 0

    next_char=sequence[0]
    next_spring=springs[0]

    out=0
    if(next_char=='#'):

        group = sequence[:next_spring].replace('?','#')
        if(group!='#'*next_spring):
            out +=0
        elif(len(sequence)==next_spring):
            if(len(springs)==1):
                out+=1
            else:
                out+=0
        elif(sequence[next_spring] in '?.'):
            out+=dynamic_spring(DP,sequence[next_spring+1:], springs[1:])

    elif(next_char=='.'):
        out=dynamic_spring(DP, sequence[1:], springs)

    elif(next_char=='?'):
        out=dynamic_spring(DP, sequence[1:], springs)

        group = sequence[:next_spring].replace('?','#')
        if(group!='#'*next_spring):
            out +=0
        elif(len(sequence)==next_spring):
            if(len(springs)==1):
                out+=1
            else:
                out+=0
        elif(sequence[next_spring] in '?.'):
            out+=dynamic_spring(DP,sequence[next_spring+1:], springs[1:])

    DP[(sequence, springs)]=out
    return out


combos=0
for line in data_raw:
    sequence,springs=line.split()
    sequence=((sequence+'?')*5)[:-1]
    springs=((springs+',')*5)[:-1]
    springs = [int(i) for i in springs.split(',')]
    springs=tuple(springs)
    DP = {}
    combos+= dynamic_spring(DP,sequence,springs)
print (combos)