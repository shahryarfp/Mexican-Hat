#!/usr/bin/env python
# coding: utf-8

# # Mexican-Hat

# In[1]:


import numpy as np
import copy
import matplotlib.pyplot as plt


# In[2]:


input_array_ = np.array([0.27, 0.35, 0.44, 0.58, 0.66, 0.77, 0.4, 0.32, 0.20, 0.15, 0.08])


# In[3]:


def activation_function(x):
    if x<0:
        return 0
    if x<2:
        return x
    else:
        return 2


# In[10]:


def Mexican_Hat(input_array, R1, R2, C1, C2, t_max):
    plot_list = []
    t = 0
    # step 2&7
    while t < t_max:
        new_list = []
        for k in range(len(input_array)):
            # step 0
            w = []
            for i in range(R1+1):
                if i > len(input_array):
                    break
                w.append(C1)
            for i in range(R1+1, R2+1):
                if i > len(input_array):
                    break
                w.append(C2)
            for i in range(R2+1, 10**7):
                if i > len(input_array):
                    break
                w.append(0)
                
            # step 3
            sum_ = 0
            for i in range(len(input_array)):
                sum_ += w[abs(i-k)]*input_array[i]
            # step 4
            new_list.append(activation_function(sum_))
        plot_list.append(new_list)
        # step 5
        input_array = copy.deepcopy(np.array(new_list))
        # step 6
        t += 1
    return plot_list, input_array


# ## A

# In[11]:


input_array = copy.deepcopy(input_array_)
R1 = 1
R2 = 10**6
C1 = 0.6
C2 = -0.4
t_max = 10

plot_list, input_array = Mexican_Hat(input_array, R1, R2, C1, C2, t_max)


# In[12]:


print('Unit with maximum value concentration:')
print(input_array_[np.argmax(input_array)])
for i in range(len(plot_list)):
    plt.plot(np.arange(0,11), plot_list[i], label = i)
    plt.legend()


# ## B

# In[13]:


input_array = copy.deepcopy(input_array_)
R1 = 1
R2 = 3
C1 = 0.6
C2 = -0.4
t_max = 10

plot_list, input_array = Mexican_Hat(input_array, R1, R2, C1, C2, t_max)


# In[14]:


print('Unit with maximum value concentration:')
print(input_array_[np.argmax(input_array)])
for i in range(len(plot_list)):
    plt.plot(np.arange(0,11), plot_list[i], label = i)
    plt.legend()


# In[ ]:




