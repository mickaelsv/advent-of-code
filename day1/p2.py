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

    similarity_score = 0
    # current_value = 0

    for i in range(len(first_list)):
        if (i==0):
            current_value = first_list[0]
            current_score = second_list.count(first_list[0])
            similarity_score = current_score * current_value
        elif (first_list[i] == current_value):
            similarity_score += current_score * current_value
        else :
            current_value = first_list[i]
            current_score = second_list.count(first_list[i])
            similarity_score += current_score * current_value

    print(similarity_score)

main()