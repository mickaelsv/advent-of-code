count = 0


def check_if_in_grid(i,j,direction,sizeI,sizeJ):
    if direction=="north":
        return (j-3>=0)
    elif direction=="northeast":
        return (j-3>=0 and i+3<sizeI)
    elif direction=="east":
        return (i+3<sizeI)
    elif direction=="southeast":
        return (j+3<sizeJ and i+3<sizeI)
    elif direction=="south":
        return (j+3<sizeJ)
    elif direction=="southwest":
        return (j+3<sizeJ and i-3>=0)
    elif direction=="west":
        return (i-3>=0)
    elif direction=="northwest":
        return (j-3>=0 and i-3>=0)

def getword(i,j,matrix,direction):
    north = [j,j-1,j-2,j-3]
    east = [i,i+1,i+2,i+3]
    south = [j,j+1,j+2,j+3]
    west = [i,i-1,i-2,i-3]
    default_i = 4*[i]
    default_j = 4*[j]
    if direction=="north":
        index_list_i = default_i
        index_list_j = north
    elif direction=="northeast":
        index_list_i = east
        index_list_j = north
    elif direction=="east":
        index_list_i = east
        index_list_j = default_j
    elif direction=="southeast":
        index_list_i = east
        index_list_j = south
    elif direction=="south":
        index_list_i = default_i
        index_list_j = south
    elif direction=="southwest":
        index_list_i = west
        index_list_j = south
    elif direction=="west":
        index_list_i = west
        index_list_j = default_j
    elif direction=="northwest":
        index_list_i = west
        index_list_j = north
    return "".join([matrix[index_list_i[index]][index_list_j[index]] for index in range(4)])


def check_count(i,j,matrix,direction,sizeI,sizeJ):
    global count
    if (matrix[i][j] == "X" and check_if_in_grid(i,j,direction,sizeI,sizeJ)):
        word = getword(i,j,matrix,direction)
        word_to_check = "XMAS"
        if word==word_to_check:
            count+=1




def count_santa(matrix):
    global count
    sizeI = len(matrix)
    sizeJ= len(matrix[0])
    for i in range(sizeI):
        for j in range(sizeJ):

            # North 
            check_count(i,j,matrix,"north",sizeI,sizeJ)

            # North-East
            check_count(i,j,matrix,"northeast",sizeI,sizeJ)
            
            # East
            check_count(i,j,matrix,"east",sizeI,sizeJ)

            # South-East
            check_count(i,j,matrix,"southeast",sizeI,sizeJ)    

            # South
            check_count(i,j,matrix,"south",sizeI,sizeJ)    
            
            # South-West
            check_count(i,j,matrix,"southwest",sizeI,sizeJ)

            # West
            check_count(i,j,matrix,"west",sizeI,sizeJ)

            # North-West
            check_count(i,j,matrix,"northwest",sizeI,sizeJ)

    return count


if __name__ == "__main__":
    with open("input", "r") as f:
        grid = [list(line.strip()) for line in f]

    # print(count)
    result = count_santa(grid)
    print(f"Total is: {result}")