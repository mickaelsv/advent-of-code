def main():
    first_list = []
    second_list = []
    file = open("input.txt", "r")
    
    # get the lines of the file in 2 lists
    for lines in file:
        tmp = lines.split("   ")
        first_list.append(int(tmp[0]))
        second_list.append(int(tmp[1]))
    
    first_list.sort()
    second_list.sort()

    sum_distance = 0

    for i in range(len(first_list)):
        sum_distance += abs(first_list[i]-second_list[i])

    print(sum_distance)

main()