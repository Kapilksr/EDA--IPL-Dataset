#!/usr/bin/env python
# coding: utf-8

# In[1]:


##import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[2]:


#read and store data in dataframe
data=pd.read_csv('matches.csv')


# In[3]:


##save data in df and read top 5 rows o fthe data to see how the data looks
df=data
df.head()


# In[4]:


## check number of rows and columns in dataset
df.shape


# In[5]:


#to eyeball all the features
df.describe(include='all')


# In[6]:


## to eyeball only numeric features
df.describe()


# In[7]:


##id column is not that important for us and dl applied should be a categorical feature


# In[8]:


df=df.drop(['id'],axis=1)


# In[9]:


df['dl_applied']=df['dl_applied'].astype('str')


# In[10]:


df.head()


# In[11]:


df.describe()


# In[12]:



df.columns


# In[13]:


# to know the frequency of men of matches awards
df['player_of_match'].value_counts()


# In[14]:


# to know the top 10 players with most number of man of matches awards
df['player_of_match'].value_counts()[0:10]


# In[15]:


## to plot bar chart of above observation
players=list(df['player_of_match'].value_counts()[0:10].keys())


# In[16]:


players


# In[17]:


awards=list(df['player_of_match'].value_counts()[0:10])


# In[18]:


awards


# In[19]:


plt.figure(figsize=(15,5))
plt.bar(players,awards)
plt.show()


# In[20]:


df.columns


# In[21]:


## to see how the result went for all the matches with counts
df['result'].value_counts()


# In[22]:


## to see which teams won most numbers of tosses
df['toss_winner'].value_counts()


# In[23]:


## too see the deatils of team winning by runs and that batted first
batting_first=df[df['win_by_runs']!=0]


# In[24]:


batting_first.head()


# In[25]:


## to plot histogram of above observation
plt.figure(figsize=(10,5))
plt.hist(batting_first['win_by_runs'],bins=7)
plt.title('Distribution of wins by runs',size=20)
plt.xlabel('Win by runs',size=15)
plt.ylabel('Frequency',size=15)
plt.show()


# In[26]:


batting_first.head()


# In[27]:


## we can check the teams with their corresponding win counts while batting first
batting_first['winner'].value_counts()


# In[28]:


## to plot this

plt.figure(figsize=(20,7))
plt.bar(list(batting_first['winner'].value_counts()[0:10].keys()),list(batting_first['winner'].value_counts()[0:10]),color='red')
plt.xticks(rotation=45,size=15)
plt.yticks(size=15)
plt.xlabel('Team',size=20)
plt.ylabel('Winning frequency while batting first',size=15)
plt.show()


# In[29]:


plt.figure(figsize=(12,12))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')

plt.show()


# In[30]:


df.columns


# In[31]:


## now we will analyze teams that won with wickets means the teams that chased the scores
batted_last=df[df['win_by_wickets']!=0]
batted_last.head()


# In[32]:


## plot histogram to see the distribution
plt.figure(figsize=(10,5))
plt.hist(batted_last['win_by_wickets'],bins=9)
plt.show()


# In[33]:


## to see the teams and number of wins while batting later is
batted_last['winner'].value_counts()


# In[34]:


## to make a bar chart for the same
plt.figure(figsize=(20,7))
plt.bar(list(batted_last['winner'].value_counts()[0:10].keys()),list(batted_last['winner'].value_counts()[0:10]))
plt.xticks(rotation=45,size=15)
plt.yticks(size=13)
plt.xlabel('Teams',size=20)
plt.ylabel('Frequency of win while batting second',size=15)
plt.show()


# In[35]:


## to plot a pie chart for the same
plt.figure(figsize=(10,10))
plt.pie(list(batted_last['winner'].value_counts()),labels=list(batted_last['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[36]:


df.columns


# In[37]:


## to analyze matches per season
df['Season'].value_counts()


# In[38]:


# to analyze matches per city
df['city'].value_counts()


# In[39]:


df.columns


# In[40]:


## to see how many times the team that won the toss won the match too
np.sum(df['toss_winner']==df['winner'])


# In[41]:


## to check the percentage
np.sum(df['toss_winner']==df['winner'])/df['toss_winner'].shape[0]


# In[42]:


## there is another dataset where we have details of batsmen
data2=pd.read_excel('Players.xlsx')


# In[43]:


df2=data2
df2.head()


# In[44]:


## to check number of rows and columns
df2.shape


# In[46]:


#3 to check the count of right handed and left handed batsman
df2['Batting_Hand'].value_counts()


# In[55]:


## we see that due to capitalization issue right handed batsman are categorized in two categories that we can change

df2['Batting_Hand']=df2['Batting_Hand'].str.replace('hand','Hand')


# In[56]:


# now we check the counts again
df2['Batting_Hand'].value_counts()


# In[59]:


## we can create pie chart for the same
plt.pie(list(df2['Batting_Hand'].value_counts()),labels=list(df2['Batting_Hand'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[60]:


## we see that nearly 3/4th of our players are right handed


# In[ ]:





# In[ ]:




