### part 1 of the day 4 of adventofcode
### https://adventofcode.com/2024/day/4

# get the word given the position and the direction
def getword(i,j,matrix,direction,sizeI,sizeJ):
    north = [j,j-1,j-2,j-3]
    east = [i,i+1,i+2,i+3]
    south = [j,j+1,j+2,j+3]
    west = [i,i-1,i-2,i-3]
    default_i = 4*[i]
    default_j = 4*[j]
    correct = True
    if direction=="north" and (j-3>=0):
        index_list_i = default_i
        index_list_j = north
    elif direction=="northeast" and (j-3>=0 and i+3<sizeI):
        index_list_i = east
        index_list_j = north
    elif direction=="east" and (i+3<sizeI):
        index_list_i = east
        index_list_j = default_j
    elif direction=="southeast" and (j+3<sizeJ and i+3<sizeI):
        index_list_i = east
        index_list_j = south
    elif direction=="south" and (j+3<sizeJ):
        index_list_i = default_i
        index_list_j = south
    elif direction=="southwest" and (j+3<sizeJ and i-3>=0):
        index_list_i = west
        index_list_j = south
    elif direction=="west" and (i-3>=0):
        index_list_i = west
        index_list_j = default_j
    elif direction=="northwest" and (j-3>=0 and i-3>=0):
        index_list_i = west
        index_list_j = north
    else:
        correct = False
    if correct:
        return "".join([matrix[index_list_i[index]][index_list_j[index]] for index in range(4)])

# count if a word in a specific direction is an XMAS or not
def check_count(i,j,matrix,direction,sizeI,sizeJ):
    if (matrix[i][j] == "X"):
        word = getword(i,j,matrix,direction,sizeI,sizeJ)
        word_to_check = "XMAS"
        if word==word_to_check:
            return 1
    return 0

# count every XMAS for every directions
def count_XMAS(matrix):
    sizeI = len(matrix)
    sizeJ= len(matrix[0])
    count=0
    for i in range(sizeI):
        for j in range(sizeJ):

            # North 
            count+=check_count(i,j,matrix,"north",sizeI,sizeJ)

            # North-East
            count+=check_count(i,j,matrix,"northeast",sizeI,sizeJ)
            
            # East
            count+=check_count(i,j,matrix,"east",sizeI,sizeJ)

            # South-East
            count+=check_count(i,j,matrix,"southeast",sizeI,sizeJ)    

            # South
            count+=check_count(i,j,matrix,"south",sizeI,sizeJ)    
            
            # South-West
            count+=check_count(i,j,matrix,"southwest",sizeI,sizeJ)

            # West
            count+=check_count(i,j,matrix,"west",sizeI,sizeJ)

            # North-West
            count+=check_count(i,j,matrix,"northwest",sizeI,sizeJ)
    return count

if __name__ == "__main__":
    with open("input", "r") as f:
        grid = [list(line.strip()) for line in f]
    result = count_XMAS(grid)
    print(f"Total is: {result}")