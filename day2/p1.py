def difference_too_high(a,b):
    return (abs(a-b)>3)

def not_changing(a,b):
    return a==b

def same_evolution(a,b,statement):
    return statement == (a-b>0)
def main():
    matrix=[]
    file = open("input", "r")
    
    for lines in file:
        matrix.append(lines.split())
    count = 0
    for lines in matrix:
        print("len",len(lines))
        lines[0] = int(lines[0])
        valid = True
        for i in range(1,len(lines)):
            print("i",i)
            lines[i] = int(lines[i])
            if (i==1):
                if (difference_too_high(lines[0],lines[1]) or not_changing(lines[0],lines[1])):
                    valid = False
                    continue
                else:
                    increasing = ((lines[1]-lines[0])>0)
                    print("this line is increasing ? ",increasing)
            else:
                if (difference_too_high(lines[i-1],lines[i]) or not_changing(lines[i-1],lines[i]) or not (same_evolution(lines[i],lines[i-1],increasing)) ):
                    print("line issue later",lines)
                    if (increasing != ((lines[i]-lines[i-1])>0)):
                        print("increasing != lines[i]-lines[i-1])>0: ",(lines[i]-lines[i-1])>0)
                        print("increasing",increasing)
                        print(increasing != (lines[i]-lines[i-1])>0)
                    valid = False
                    continue

        if (valid):
            count+=1
        print(lines)
    print(count)

main()