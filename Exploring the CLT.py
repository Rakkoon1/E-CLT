
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

plt.hist(pop1, alpha=0.5, label='P1')
plt.hist(pop2, alpha=0.5, label='P2')
plt.legend(loc='upper right')
plt.show()


# In[3]:


s1 = np.random.choice(pop1, 100, replace=True)
s2 = np.random.choice(pop2, 100, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()


# In[4]:


print(s1.mean())
print(s2.mean())
print(s1.std())
print(s2.std())

diff=s2.mean()-s1.mean()
print(diff)


# In[5]:


size = np.array([len(s1), len(s2)])
std = np.array([s1.std(), s2.std()])

diff2 = (sum(std ** 2/ size)) ** 0.5
print(diff2)
print(diff/diff2)


# In[6]:


from scipy.stats import ttest_ind
print(ttest_ind(s2, s1, equal_var=False))


# 1. Increasing the sample size can increase the amount of variance between samples.

# In[7]:


s1 = np.random.choice(pop1, 1000, replace=True)
s2 = np.random.choice(pop2, 1000, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()
print(format("Sample 1 Mean:"), s1.mean())
print(format("Sample 2 Mean:"), s2.mean())
print(format("Sample 1 STD:"), s1.std())
print(format("Sample 2 STD:"), s2.std())


# In[8]:


s1 = np.random.choice(pop1, 20, replace=True)
s2 = np.random.choice(pop2, 20, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()
print(format("Sample 1 Mean:"), s1.mean())
print(format("Sample 2 Mean:"), s2.mean())
print(format("Sample 1 STD:"), s1.std())
print(format("Sample 2 STD:"), s2.std())


# 1(2). All the values changed at different rates: The sample mean for s1 increased from 2.006 to 2.2, the sample mean for s2 increased at a lower rate of change from 4.893 to 4.9, the STD of s1 decreased from 1.32 to 1.56, the STD of s2 decreased at a higher rate of change from 1.53 to 0.99

# Part 2

# In[19]:


pop1 = np.random.binomial(10, 0.3, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

plt.hist(pop1, alpha=0.5, label='P1')
plt.hist(pop2, alpha=0.5, label='P2')
plt.legend(loc='upper right')
plt.show()


# In[20]:


s1 = np.random.choice(pop1, 100, replace=True)
s2 = np.random.choice(pop2, 100, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()


# In[21]:


print(s1.mean())
print(s2.mean())
print(s1.std())
print(s2.std())

diff=s2.mean()-s1.mean()
print(diff)


# In[22]:


size = np.array([len(s1), len(s2)])
std = np.array([s1.std(), s2.std()])

diff2 = (sum(std ** 2/ size)) ** 0.5
print(diff2)
print(diff/diff2)


# In[23]:


print(ttest_ind(s2, s1, equal_var=False))


# 2. Because the p-values are closer together I expect the rate of change to be much closer.

# In[24]:


pop1 = np.random.binomial(10, 0.4, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

plt.hist(pop1, alpha=0.5, label='P1')
plt.hist(pop2, alpha=0.5, label='P2')
plt.legend(loc='upper right')
plt.show()


# In[25]:


s1 = np.random.choice(pop1, 100, replace=True)
s2 = np.random.choice(pop2, 100, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()


# In[26]:


print(s1.mean())
print(s2.mean())
print(s1.std())
print(s2.std())

diff=s2.mean()-s1.mean()
print(diff)


# In[27]:


size = np.array([len(s1), len(s2)])
std = np.array([s1.std(), s2.std()])

diff2 = (sum(std ** 2/ size)) ** 0.5
print(diff2)
print(diff/diff2)


# In[28]:


print(ttest_ind(s2, s1, equal_var=False))


# 2(2). With the value for 'p' closer together, the t-value significantly reduced from 9.25 to 4.15 and the p-value increased from 3.6 to 4.8, meaning that the data significantly reduced the amount of noise but it became less likely that we can find a meaningful difference between the populations.

# Part 3. Changing to a gamma distribution I expect the graphs to skew to the right, meaning that the mean and standard deviation will represents values on the lower end of the scales.

# In[34]:


pop1 = np.random.gamma(20, 3, 10000)
pop2 = np.random.gamma(20, 4, 10000)

plt.hist(pop1, alpha=0.5, label='P1')
plt.hist(pop2, alpha=0.5, label='P2')
plt.legend(loc='upper right')
plt.show()


# In[35]:


s1 = np.random.choice(pop1, 1000, replace=True)
s2 = np.random.choice(pop2, 1000, replace=True)
plt.hist(s1, alpha=0.5, label='S1')
plt.hist(s2, alpha=0.5, label='S2')
plt.legend(loc='upper right')
plt.show()


# In[36]:


print(s1.mean())
print(s2.mean())
print(s1.std())
print(s2.std())


# 3(2). Yes, the sample mean values are accurately represented, but I did not expect the standard deviation values to be above 10.
