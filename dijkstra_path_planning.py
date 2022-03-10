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




