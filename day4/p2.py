### part 2 of the day 4 of adventofcode
### https://adventofcode.com/2024/day/4

# check if a coordinate is in the grid or not
def check_if_in_grid(i,j,direction,sizeI,sizeJ):
    return ((1<= j < sizeJ-1) and (1<= i < sizeI-1))

# get the word given the position and the direction
def getword(i,j,matrix,direction):
    index_list_i = [i-1,i,i+1]
    if direction=="diag1":
        index_list_j = [j+1,j,j-1]
    elif direction=="diag2":
        index_list_j = [j-1,j,j+1]
    return "".join([matrix[index_list_i[index]][index_list_j[index]] for index in range(3)])

# check if there is a diag writing MAS for a specific direction
def check_count(i,j,matrix,direction,sizeI,sizeJ):
    global count
    if (matrix[i][j] == "A" and check_if_in_grid(i,j,direction,sizeI,sizeJ)):
        word = getword(i,j,matrix,direction)
        if "M" in word and "S" in word:
            return 1
    return 0

# count if you have an "X" writting MAS, for example:
# M . M
# . A .
# S . S
def count_MAS_diag(matrix):
    
    final_count = 0 
    sizeI = len(matrix)
    sizeJ= len(matrix[0])
    for i in range(sizeI):
        for j in range(sizeJ):
            count_during_iteration = 0

            count_during_iteration+=check_count(i,j,matrix,"diag1",sizeI,sizeJ)

            count_during_iteration+=check_count(i,j,matrix,"diag2",sizeI,sizeJ)    

            # We need to add a count only both diagonals are corrects
            if(count_during_iteration==2):
                final_count+=1

    return final_count


if __name__ == "__main__":
    with open("input", "r") as f:
        grid = [list(line.strip()) for line in f]

    # print(count)
    result = count_MAS_diag(grid)
    print(f"Total is: {result}")