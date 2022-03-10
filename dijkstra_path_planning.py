#Importing necessary libraries
import numpy as np
import cv2 as cv
import copy


# In[76]:


#Function that checks if the node is in the obstacle space of obstacle 1
def obstacle1(node):
    '''
    Input:
    node    : tuple(x, y)

    Output:
    True if the node is in obstacle space
    False if the node is not in obstacle space
    '''
    if ((node[1]<=(0.3165*node[0]+178.85)) and (node[1]>=(-1.232*node[0]+221.43))):
        if (node[1]<=(-3.2*node[0]+452.76)):
            return True
        elif (node[1]>=(0.857*node[0]+104.87)):
            return True 
    else:
        return False


# In[77]:


#Function that checks if the node is in the obstacle space of obstacle 2
def obstacle2(node):
    '''
    Input:
    node    : tuple(x, y)

    Output:
    True if the node is in obstacle space
    False if the node is not in obstacle space
    '''
    if ((node[0]>=160) and (node[1]>=(-0.58*node[0]+169.8)) and (node[1]>=(0.58*node[0]-62.29)) and (node[0]<=240) and (node[1]<=(-0.58*node[0]+262.2)) and (node[1]<=(0.58*node[0]+30.2))):
        return True
    else:
        return False


# In[78]:


#Function that checks if the node is in the obstacle space of obstacle 3
def obstacle3(node):
    '''
    Input:
    node    : tuple(x, y)

    Output:
    True if the node is in obstacle space
    False if the node is not in obstacle space
    '''
    if (((node[0]-300)**2 + (node[1]-185)**2) <= (45**2)):
        return True
    else:
        return False


# In[100]:


#Function that checks if the node maintains clearance at the boundaries
def obstacle4(node):
    '''
    Input:
    node    : tuple(x, y)

    Output:
    True if the node is in obstacle space
    False if the node is not in obstacle space
    '''
    if node[0]<=5 or node[0]>=395 or node[1]<=5 or node[1]>=245:
        return True
    else:
        return False


# In[101]:


#Function that checks if the node is in the obstacle space of any of the three obstacles
def obstacle_space(node):
    '''
    Input:
    node    : tuple(x, y)

    Output:
    True if the node is in obstacle space
    False, if the node is not in obstacle space
    '''
    if obstacle1(node) or obstacle2(node) or obstacle3(node) or obstacle4(node):
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
    if node[0]!=1:
        child_node = ((node[0]-1), node[1])
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[83]:


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
    if node[0]!=400:
        child_node = ((node[0]+1), node[1])
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[84]:


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
    if node[1]!=250:
        child_node = ((node[0]), node[1]+1)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[85]:


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
    if node[1]!=1:
        child_node = ((node[0]), node[1]-1)
        child_node_info = [node, (node_info[1] + 1)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[86]:


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
    if node[0]!=1 and node[1]!=250:
        child_node = ((node[0]-1), node[1]+1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[87]:


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
    if node[0]!=400 and node[1]!=250:
        child_node = ((node[0]+1), node[1]+1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[88]:


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
    if node[0]!=1 and node[1]!=1:
        child_node = ((node[0]-1), node[1]-1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info


# In[89]:


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
    if node[0]!=400 and node[1]!=1:
        child_node = ((node[0]+1), node[1]-1)
        child_node_info = [node, (node_info[1] + 1.4)]
        return True, child_node, child_node_info
    else:
        return False, node, node_info

#Function that determines if the newly generated node should be added in the open list or should the cost to come and parent be
#changed of the existing node
def decisionOnNode(obstacle_space, node, node_info, open_list, closed_list):
    '''
    Input:
    obstacle_space : function that defines the obstacle space
    node           : tuple(x, y)
    node_info      : list[parent_node, cost_to_come]
    open_list      : dictionary of all open nodes
    closed_list    : dictionary of all closed nodes
    
    Output:
    Node with lowest cost to come
    '''
    if not obstacle_space(node):
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
def visualization(img_map, obstacle_space, visited_node, optimal_path):
    '''
    Input:
    img_map        : image array of size 250x400
    obstacle_space : function that defines the obstacle space
    visited_node   : list of all visited nodes
    optimal_path   : path from goal node to start node
    
    Output:
    "project2.avi" video file stored in the project folder
    '''
    print("Generating video output named 'project2'...\n")
    out = cv.VideoWriter('project2.avi',cv.VideoWriter_fourcc(*'XVID'), 3000, (400,250))
    for y in range(img_map.shape[0]):
        for x in range(img_map.shape[1]):
            node = (x, y)
            if obstacle_space(node):
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
    out.release()
    print("Video output generated")
