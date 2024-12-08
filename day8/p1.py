### part 1 of the day 8 of adventofcode
### https://adventofcode.com/2024/day/8

# Get the antennas of the grid, ie every points in the grid that are not "."
def getAntennas(grid,width,height):
    antennas = []
    for i in range(width):
        for j in range(height):
            if grid[i][j]!=".":
                antennas.append([grid[i][j],i,j])
    return antennas

# get the pairs of antennas.
# Two antennas are a pair if their symbol is the same, example first antenna is 'A',48,48, second is 'A',27,27 : 
# it's a pair because they have the same symbol
def createPairs(antennas):
    antennasPairs = []
    n = len(antennas)
    for i in range(n):
        for j in range(i):
            if (i != j) and (antennas[i][0] == antennas[j][0]):
                antennasPairs.append([antennas[i],antennas[j]]) 
    return antennasPairs

# check if a given point is in the grid
def check_point_in_grid(point,width,height):
    return 0<=point[1]<width and 0<=point[2]<height

# a special addition of two vectors.
# a is in the form "'A',48,48", b in the form "48,48"
def add_vec(a,b):
    return [a[0], a[1] + b[0], a[2] + b[1]]

# get the opposite of a vector
def minus(coordinate):
    return [-coordinate[0],-coordinate[1]]

# get the positions of the antinodes given the conditions of the test
def getPositionOfAntinodes(pair,width,height):
    # get vector of pair1-pair2
    vector_between_pair = [pair[0][1]-pair[1][1], pair[0][2]-pair[1][2]]
    antinodes = []
    # if you add the vector
    coordinate_first_antinode = add_vec(pair[0],vector_between_pair)
    # if you add -vector
    coordinate_second_antinode = add_vec(pair[1],minus(vector_between_pair))

    # if they are in grid, add them to the antinodes list
    if check_point_in_grid(coordinate_first_antinode,width, height):
        antinodes.append(coordinate_first_antinode)
    if check_point_in_grid(coordinate_second_antinode,width, height):
        antinodes.append(coordinate_second_antinode)
    return antinodes

# concatenate the list of every antinodes of every pairs
def getAntinodes(antennasPairs, width, height):
    antinodes = []
    for pairs in antennasPairs:
        antinodes+=getPositionOfAntinodes(pairs,width,height)
    return antinodes

# given the antinodes positions, make it a set without considering their symbol, so you count the unique locations.
def count_unique_locations(antinodes):
    unique_locations = {(point[1], point[2]) for point in antinodes}
    count = len(unique_locations)
    return count

if __name__ == "__main__":
    with open("input", "r") as f:
        grid = [list(line.strip()) for line in f]
    result = 0
    width = len(grid)
    height = len(grid[0])
    antennas = getAntennas(grid,width,height)
    antennasPairs = createPairs(antennas)
    antinodes = getAntinodes(antennasPairs,width,height)
    result = count_unique_locations(antinodes)
    print(f"Total is: {result}")