### part 1 of the day 3 of adventofcode
### https://adventofcode.com/2024/day/3

import re 
# sum up every "mul(X,Y)" = X \times Y for every mul(X,Y) in the file
def calculate_total(input):
    processed_line = re.findall(r"mul\(([0-9]+),([0-9]+)\)",input)
    result = sum([(int(processed_line[i][0])*int(processed_line[i][1])) for i in range(len(processed_line))])
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        input = f.read()
    result = calculate_total(input)
    print(f"Total is: {result}")