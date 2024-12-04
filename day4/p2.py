count = 0

final_count = 0


def check_if_in_grid(i,j,direction,sizeI,sizeJ):
    return ((1<= j < sizeJ-1) and (1<= i < sizeI-1))

def getword(i,j,matrix,direction):
    # considering the "S" is the arrow of compass
    north = [j+1,j,j-1]
    east = [i-1,i,i+1]
    south = [j-1,j,j+1]
    west = [i+1,i,i-1]
    if direction=="northeast":
        index_list_i = east
        index_list_j = north
    elif direction=="southeast":
        index_list_i = east
        index_list_j = south
    elif direction=="southwest":
        index_list_i = west
        index_list_j = south
    elif direction=="northwest":
        index_list_i = west
        index_list_j = north
    return "".join([matrix[index_list_i[index]][index_list_j[index]] for index in range(3)])


def check_count(i,j,matrix,direction,sizeI,sizeJ):
    global count
    if (check_if_in_grid(i,j,direction,sizeI,sizeJ)):
        word = getword(i,j,matrix,direction)
        word_to_check = "MAS"
        if word==word_to_check:
            count+=1




def count_santa(matrix):
    global count
    global final_count
    sizeI = len(matrix)
    sizeJ= len(matrix[0])
    for i in range(sizeI):
        for j in range(sizeJ):

            # North-East
            check_count(i,j,matrix,"northeast",sizeI,sizeJ)

            # South-East
            check_count(i,j,matrix,"southeast",sizeI,sizeJ)    

            # South-West
            check_count(i,j,matrix,"southwest",sizeI,sizeJ)

            # North-West
            check_count(i,j,matrix,"northwest",sizeI,sizeJ)

            # We need to add a count only if we got 2 check, for the 2 diagonals
            if(count==2):
                final_count+=1
            count = 0

    return final_count


if __name__ == "__main__":
    with open("input", "r") as f:
        grid = [list(line.strip()) for line in f]

    # print(count)
    result = count_santa(grid)
    print(f"Total is: {result}")