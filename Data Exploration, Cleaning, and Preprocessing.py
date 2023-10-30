#!/usr/bin/env python
# coding: utf-8

# In[126]:


######### Data Exploration, Cleaning, and Preprocessing##########


# In[ ]:





# In[ ]:


import pandas as pd


# In[127]:


df=pd.read_csv(r'D:\Data Analytics project\renewable_Electricity_project\renewable electricity by country.csv', header=0)


# In[128]:


df_country=pd.read_csv(r'D:\Data Analytics project\renewable_Electricity_project\Country_data.csv', header=0)


# In[129]:


df.head()   #to check the content and structure of the data frame


# In[130]:


df_country.head()            #to check the content and structure of the second data frame


# In[131]:


df.info()            #to see the data information type and count


# In[132]:


df.describe()         #to see the basic statistics


# In[133]:


### ploting a line chart to see the dirstribution of the three numeric columns


# In[134]:


import matplotlib.pyplot as plt


# In[135]:


plt.plot(df['non-hydro renewables Gwh'], marker='o')


# In[136]:


plt.plot(df['all electricity generation Gwh'], marker='o')


# In[137]:


plt.plot(df['all renewables Gwh'], marker='o')


# In[138]:


df=df.drop(['Notes','Source'],axis=1)       # to drop the note and source columns because they dont have any use in the analysis


# In[139]:


df.head()                             # checking if the two columns has droped


# In[140]:


df.isnull().sum         #checking if there is null value


# In[141]:


df = df.loc[~(df.iloc[:, 1:] == 0).all(axis=1)]     #droping raws with all the columns has zero value except the first column


# In[142]:


df['all_renewables_Gwh / all_electricity_generation_Gwh']=df['all renewables Gwh']/df['all electricity generation Gwh']     # creating a new column of ratio of renewable to the all electricity generation


# In[143]:


df['non-hydro renewables Gwh/all_electricity_generation_Gwh']=df['non-hydro renewables Gwh']/df['all electricity generation Gwh']   # creating a new column of ratio of no-hydro renewable to the all electricity generation


# In[144]:


merged_data=pd.merge(df,df_country,left_on='Country',right_on='name',how='inner')  #merging the two data frame to have


# In[145]:


merged_data.head()           #checking the merged data


# In[146]:


merged_data.info()    #to see the data information type and count


# In[148]:


merged_data=merged_data.drop(['name'],axis=1)     # droping the name column because its duplication of the country column


# In[150]:


merged_data.head()        #checking the merged data  after dropping the name column


# In[153]:


merged_data.to_csv('D:/Data Analytics project/renewable_Electricity_project/merged_data.csv',index=False)


# In[ ]:




