#!/usr/bin/env python
# coding: utf-8

# This will create a DB named `books`, if it doesn't exist and switch to that DB. But the DB will not be listed in the show dbs until the database has some data because in Mongo the database is in the form of a file. The file is not created until the collections are created.

# In[12]:


#Uncomment the following line and install pymongo if you don't have pymongo already.
#Alternatively, if you are using Anaconda, you can run 
get_ipython().system('pip install pymongo')


# In[13]:


from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')


# In[14]:


#This will create a Collection/Database called books if it doesn't already exist
db = client['books']


# In[15]:


books = db.books


# In[16]:


books.insert_one({"author": "Sidney Sheldon",
            "about": "Tell Me Your Dreams",
            "tags":
                ["MPD", "Murder", "Mystery"]})


# In[17]:


#This line will find all of books information that was inserted by the previous line.
books.find_one()

