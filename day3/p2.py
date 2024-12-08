### part 2 of the day 3 of adventofcode
### https://adventofcode.com/2024/day/3

import re 

# sum up every "mul(X,Y)" = X \times Y for every mul(X,Y) in the file 
# Only if they are in a "do()", else if they are in a "dont()", don't add them.
# for example do()mul(1,3)don't()mul(3,8) should return 1*3 = 3.
def calculate_total(input):
    processed_line = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)",input)
    do = True
    result = 0
    for sentence in processed_line:
        if (sentence == 'do()'):
            do = True
        elif (sentence == "don't()"):
            do = False
        else:
            if do:
                multiply = re.findall(r"mul\(([0-9]+),([0-9]+)\)",sentence)
                if (multiply != []):
                    result+=(int(multiply[0][0])*int(multiply[0][1]))
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        input = f.read()
    result = calculate_total(input)
    print(f"Total is: {result}")