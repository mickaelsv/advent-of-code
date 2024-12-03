import re 
def calculate_total(input):
    processed_line = re.findall(r"mul\(([0-9]+),([0-9]+)\)",input)
    result = sum([(int(processed_line[i][0])*int(processed_line[i][1])) for i in range(len(processed_line))])
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        input = f.read()
    result = calculate_total(input)
    print(f"Total is: {result}")