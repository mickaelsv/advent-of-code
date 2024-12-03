import re 
def calculate_total(input):
    processed_line = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)",input)
    # result = sum([(int(processed_line[i][0])*int(processed_line[i][1])) for i in range(len(processed_line))])
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