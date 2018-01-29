
# coding: utf-8

# ### Problem Statement
# 
# Write a Python Program to print the given string in the format specified in the sample
# output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# WE, THE PEOPLE OF INDIA,
#       having solemnly resolved to constitute India into a SOVEREIGN, !
#             SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#              and to secure to all its citizens:

# In[59]:


given_string = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"


# In[60]:


given_string=given_string.replace("INDIA,","INDIA,\n\t")
given_string=given_string.replace("SOVEREIGN,","SOVEREIGN,!\n\t\t")
given_string=given_string.replace("REPUBLIC","REPUBLIC\n\t\t ")
given_string=given_string.replace("citizens","citizens:")


# In[61]:


print(given_string)

