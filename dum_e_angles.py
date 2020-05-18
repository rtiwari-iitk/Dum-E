#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import math as m
#input format has been assumed to be position of point 0, position of point 2, length of arm 1, length of arm 2
pos2 = []
pos0 = []
for i in (0, 1):
    pos0.append(float(input()))
for i in (0, 1):
    pos2.append(float(input()))
length1 = float(input())
length2 = float(input())
pos0 = np.asarray(pos0)
pos2 = np.asarray(pos2)
offset = pos0
pos2 = pos2 - pos0
pos0 = pos0 - pos0
length3 = ((pos2[0]**2)+(pos2[1]**2))**0.5
# print (length1, length2, length3)
# print(pos2)
gamma = m.atan(pos2[1]/pos2[0])
alpha1 = m.acos(((length3**2)+(length2**2)-(length1**2))/(2*length2*length3))
alpha3 = m.acos(((length1**2)+(length2**2)-(length3**2))/(2*length1*length2))
theta1 = gamma - alpha1
theta2 = np.pi - alpha3
pos1 = np.zeros(2)
pos1[0] = length1*m.cos(theta1)
pos1[1] = length1*m.sin(theta1)
pos1 = pos1+offset
print ('theta 1: ' , theta1, '\ntheta2: ' , theta2, '\npoint 1 x,y = ' , pos1)


# In[ ]:




