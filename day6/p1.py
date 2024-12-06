def getInitialPosition(input,possible_rotations,sizeI,sizeJ):
    for i in range(sizeI):
        for j in range(sizeJ):
            if input[i][j] in possible_rotations:
                return [i,j,input[i][j]]
    
def rotate(current_position,possible_rotations):
    for i in range (len(possible_rotations)):
        if possible_rotations[i] == current_position[2]:
            index = i
    return [current_position[0],current_position[1],possible_rotations[(index+1)%4]]

# returns the new current_position after walking and a boolean telling if you left the labyrinth or not.
def walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited):
    match current_position[2],input[current_position[0]][current_position[1]]:
        case (_,"#"):
            match current_position[2]:
                case '^':
                    current_position[0]+=1
                case 'v':
                    current_position[0]-=1
                case '>':
                    current_position[1]-=1
                case '<':
                    current_position[1]+=1
            current_position = rotate(current_position,possible_rotations)
            return current_position,False,visited
        case ("^",_):
            if [current_position[0],current_position[1]] not in visited:
                visited.append([current_position[0],current_position[1]])
            if current_position[0]==0:
                return current_position,True,visited
            else:
                current_position[0]-=1
                return walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited)
        case (">",_):
            if [current_position[0],current_position[1]] not in visited:
                visited.append([current_position[0],current_position[1]])
            if current_position[1]==sizeJ:
                return current_position,True,visited
            else:
                current_position[1]+=1
                return walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited)
        case ("v",_):
            if [current_position[0],current_position[1]] not in visited:
                visited.append([current_position[0],current_position[1]])
            if current_position[0]==sizeI:
                return current_position,True,visited
            else:
                current_position[0]+=1
                return walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited)
        case ("<",_):
            if [current_position[0],current_position[1]] not in visited:
                visited.append([current_position[0],current_position[1]])
            if current_position[1]==0:
                
                return current_position,True,visited
            else:
                current_position[1]-=1
                return walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited)
        case _ :
            print("Error in walk_until_obstacle !")

def walk_until_leave(input,current_position,possible_rotations,sizeI,sizeJ):
    visited = []
    walk,has_left,visited= walk_until_obstacle(input,current_position,possible_rotations,sizeI,sizeJ,visited)
    while (not(has_left)):
        walk,has_left,visited = walk_until_obstacle(input,walk,possible_rotations,sizeI,sizeJ,visited)
    return len(visited)

if __name__ == "__main__":
    with open("input", "r") as f:
        input =[list(line.strip()) for line in f]
    sizeI = len(input)-1
    sizeJ = len(input[0])-1
    possible_rotations=["^",">","v","<"]
    current_position = getInitialPosition(input,possible_rotations,sizeI,sizeJ)
    result = walk_until_leave(input,current_position,possible_rotations,sizeI,sizeJ)
    print(f"Total is: {result}")