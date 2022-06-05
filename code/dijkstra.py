#Importing necessary libraries
import numpy as np
import cv2 as cv
import copy

#Function that checks if the node is in the obstacle space of any of the three obstacles
def in_obstacle_space(node):
    '''
    Input:
    node    : tuple(x, y, theta)

    Output:
    True if node is in the obstacle space
    False, if node is not in the obstacle space
    '''
    obstacle1 = False
    obstacle2 = False
    obstacle3 = False
    
    x, y = node
    
    if y <= (0.32 * x + 173.2) and y >= (-1.23 * x + 229.28):
        if y <= (-3.2 * x + 436):
            obstacle1 = True
        elif y >= (0.86 * x + 111.1):
            obstacle1 = True 
      
    if (x >=165 and y >= (-0.58 * x + 175.58) and y >= (0.58 * x - 56.42) and (x <= 235) and 
       y <= (-0.58 * x + 256.51) and y <= (0.58 * x +24.42)) :
        obstacle2 = True
    
    if ((x - 300)**2 + (y - 185)**2 <= 40**2):
        obstacle3 = True
        
    if obstacle1 or obstacle2 or obstacle3:
        return True
    else:
        return False

#Function that checks if the node is in the clearance space of any of the three obstacles
def in_clearance_space(node):
    '''
    Input:
    node    : tuple(x, y, theta)

    Output:
    True if node is in the clearance space
    False, if node is not in the clearance space
    '''
    clearance1 = False
    clearance2 = False
    clearance3 = False
    clearance4 = False
    
    x, y = node
    
    if (y <= (0.32 * x + 178.85) and y >= (-1.23 * x + 221.43)):
        if y <= (-3.2 * x + 452.76):
            clearance1 = True
        elif y >= (0.86 * x + 104.87):
            clearance1 = True 
      
    if (x >= 160 and y >= (-0.58 * x + 169.8) and y >= (0.58 * x-62.29) and x <= 240 and 
       y <= (-0.58 * x + 262.2) and y <= (0.58 * node[0] + 30.2)):
        clearance2 = True
    
    if ((x-300)**2 + (y-185)**2 <= 45**2):
        clearance3 = True
        
    if x <=5 or x >= 395 or y <= 5 or y > 245:
        clearance4 = True
        
    if clearance1 or clearance2 or clearance3 or clearance4:
        return True
    else:
        return False

#Function to move the node to the left
def ActionMoveLeft(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False, node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 1:
        child_node = (x - 1, y)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node to the right
def ActionMoveRight(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 400:
        child_node = (x + 1, y)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node up
def ActionMoveUp(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if y != 250:
        child_node = (x, y + 1)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node down
def ActionMoveDown(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if y != 1:
        child_node = (x, y - 1)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node one position up and one position left
def ActionMoveUpLeft(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 1 and y != 250:
        child_node = (x - 1, y + 1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node one position up and one position right
def ActionMoveUpRight(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 400 and y != 250:
        child_node = (x + 1, y + 1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node one position down and one position left
def ActionMoveDownLeft(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 1 and y != 1:
        child_node = (x - 1, y - 1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function to move the node one position down and one position right
def ActionMoveDownRight(node, node_info):
    '''
    Input:
    node      : tuple(x, y)
    node_info : list[parent_node, cost_to_come]
    
    Output:
    True, child_node, child_node_info if the action is successful
    False node, node_info if the action is unsuccessful
    '''
    x, y = node
    if x != 400 and y != 1:
        child_node = (x + 1, y - 1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function that determines if the newly generated node should be added in the open list or 
# should the cost to come and parent be changed of the existing node
def decisionOnNode(in_clearance_space, node, node_info, open_list, closed_list):
    '''
    Input:
    in_obstacle_space : function that defines the clearance space
    node              : tuple(x, y)
    node_info         : list[parent_node, cost_to_come]
    open_list         : dictionary of all open nodes
    closed_list       : dictionary of all closed nodes
    
    Output:
    Node with lowest cost to come
    '''
    if not in_clearance_space(node):
        if node not in closed_list.keys():
            if node in open_list.keys():
                if open_list[node][1] > node_info[1]:
                    open_list[node][0] = node_info[0]
                    open_list[node][1] = node_info[1]
            else:
                open_list[node] = node_info 

#Function that returns the node with lowest cost to come in the open list
def nodeWithLowestC2C(open_list):
    '''
    Input:
    open_list : dictionary of all open nodes
    
    Output:
    Node with lowest cost to come
    '''
    node, min_= next(iter(open_list.items()))
    min_c2c = min_[1]
    
    for i in open_list:
        if min_c2c > open_list[i][1]:
            min_c2c = open_list[i][1]
            node = i
        else:
            continue
    return node

#Function that performs backtracking to find a path from the start node to the goal node
def backtracking(closed_list):
    '''
    Input:
    closed_list : dictionary of all closed nodes
    
    Output:
    path : list[nodes from goal node to start node]
    '''
    path = []
    goal = list(closed_list)[-1]
    path.append(goal)
    
    while True:
        parent = closed_list[goal][0]
        
        if parent == None:
            break 
            
        path.append(parent)
        goal = parent
        
    return path

#Function that removes duplicate elements of a list
def removeDuplicate(visited_node):
    '''
    Input:
    visited_node : list[]
    
    Output:
    visited_node : list[] with duplicate elements removed
    '''
    seen = set()
    seen_add = seen.add
    return [x for x in visited_node if not (x in seen or seen_add(x))]

#Function that visualizes the output of Dijkstra algorithm by generating a .avi video file
def visualization(img_map, in_obstacle_space, visited_node, optimal_path):
    '''
    Input:
    img_map           : image array of size 250x400
    in_obstacle_space : function that defines the obstacle space
    visited_node      : list of all visited nodes
    optimal_path      : path from goal node to start node
    
    Output:
    "dijkstra.avi" video file stored in the project folder
    '''
    print("Generating video output named 'dijkstra'...\n")
    out = cv.VideoWriter('dijkstra.avi', cv.VideoWriter_fourcc(*'XVID'), 3000, (400,250))
    for y in range(img_map.shape[0]):
        for x in range(img_map.shape[1]):
            node = (x, y)
            if in_obstacle_space(node):
                img_map[y-1][x-1] = [0, 0, 255]
            else:
                img_map[y-1][x-1] = [0, 0, 0]
    
    for i in visited_node:
        img_map[i[1]-1][i[0]-1] = [255, 255, 255]
        a = cv.flip(img_map, 0)
        out.write(a)
    
    path = copy.deepcopy(optimal_path)   
    for i in range(len(path)):
        node = path.pop()
        img_map[node[1]-1][node[0]-1] = [0, 0, 0]       
        a = cv.flip(final_map, 0)
        out.write(a)
        i+=1
    cv.imwrite('path.png', a)
    out.release()
    print("Video output generated.")
    
while True:
    x = int(input("Enter start node's x co-ordinate in the range 1-400: "))
    y = int(input("Enter start node's y co-ordinate in the range 1-250: "))
    start_node = (x, y)
    if in_clearance_space(start_node):
        print("\nThe start node is in the obstacle space. Please try again.\n")
    else:
        print("\nStart node accepted\n")
        break
while True:
    x = int(input("Enter goal node's x co-ordinate in the range 1-400: "))
    y = int(input("Enter goal node's y co-ordinate in the range 1-250: "))
    goal_node = (x, y)
    if in_clearance_space(goal_node):
        print("\nThe goal node is in the obstacle space. Please try again.\n")
    else:
        print("\nGoal node accepted\n")
        break

open_list = {}
open_list[start_node] = [None, 0]
closed_list = {}
node_index = 1
visited_node = []
visited_node.append(start_node)
count = 0

while True:
    node = nodeWithLowestC2C(open_list)
    node_info = open_list.pop(node)
    closed_list[node] = node_info

    if (node == goal_node):
        print("Goal node reached\n")
        break

    action_success, new_node, new_node_info = ActionMoveLeft(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveRight(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveUp(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveDown(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveUpLeft(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveUpRight(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveDownLeft(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)

    action_success, new_node, new_node_info = ActionMoveDownRight(node, node_info)
    if action_success:
        decisionOnNode(in_clearance_space, new_node, new_node_info, open_list, closed_list)
        visited_node.append(new_node)
    
    count += 1
    if (not bool(open_list)) and count==100000:
            print("No solution found")
            break

optimal_path = backtracking(closed_list)
final_map = np.zeros((250, 400, 3), dtype = np.uint8)
visited_node = removeDuplicate(visited_node)
visualization(final_map, in_obstacle_space, visited_node, optimal_path)