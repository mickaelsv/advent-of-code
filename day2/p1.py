### part 1 of the day 2 of adventofcode
### https://adventofcode.com/2024/day/2

# list of conditions to check

# if your difference is too high
def difference_too_high(a,b):
    return (abs(a-b)>3)

# if you're not changing
def not_changing(a,b):
    return a==b

# if you're only going up or going down
def same_evolution(a,b,statement):
    return statement == (a-b>0)

def main():
    matrix=[]
    file = open("input", "r")
    
    for lines in file:
        matrix.append(lines.split())
    count = 0
    for lines in matrix:
        lines[0] = int(lines[0])
        valid = True

        for i in range(1,len(lines)):
            lines[i] = int(lines[i])
            # if you are checking first line, you set your statement
            if (i==1):
                if (difference_too_high(lines[0],lines[1]) or not_changing(lines[0],lines[1])):
                    valid = False
                    continue
                else:
                    increasing = ((lines[1]-lines[0])>0)
            # else, check if the conditions are corrects
            else:
                if (difference_too_high(lines[i-1],lines[i]) or not_changing(lines[i-1],lines[i]) or not (same_evolution(lines[i],lines[i-1],increasing)) ):
                    if (increasing != ((lines[i]-lines[i-1])>0)):
                    valid = False
                    continue
        # if your whole line is valid
        if (valid):
            count+=1
    print(count)

main()