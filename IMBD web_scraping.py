#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])


# In[2]:


from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


# In[3]:


# extract all the div containers that have a class attribute 
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))


# In[7]:


#Extracting the data for a single movie
movie_containers[0]


# In[9]:


#name of the movie
first_movie = movie_containers[0]
first_movie.div


# In[10]:


first_movie.h3


# In[11]:


first_movie.a


# In[12]:


first_name=first_movie.h3.a.text
first_name


# In[14]:


#year
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year
first_year = first_year.text
first_year


# In[15]:


#rating
first_rating = first_movie.find('div', class_='inline-block ratings-imdb-rating' )
first_rating = first_rating.text
print(first_rating)


# In[16]:


#meta_score
first_score = first_movie.find('span', class_ ='metascore favorable')
print(first_score.text)


# In[17]:


#no. of votes
first_votes = first_movie.find('span', attrs = {'name':'nv'})     #there is one other tag that is similar to it but since
print(first_votes.text)                                           # .find fn only returns the first value
print(first_votes['data-value'])                                  # AND there is a different way of finding things in name


# In[21]:


#combining all
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_containers:
    if container.find('span',class_='metascore favorable') is not None:
        name=container.h3.a.text
        names.append(name)
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
        rating=float(container.find('div', class_='inline-block ratings-imdb-rating' ).text)
        imdb_ratings.append(rating)
        vote=container.find('span', attrs = {'name':'nv'})['data-value']  #Here we donot want to get text we want to find the 
        votes.append(vote)                                                    # actual no of votes
        m_score = container.find('span', class_ ='metascore favorable').text
        metascores.append(int(m_score))


# In[22]:


import pandas as pd
test_df = pd.DataFrame({'movie':names,
                        'year':years,
                       'imdb':imdb_ratings,
                       'metascore':metascores,
                       'votes':votes})                                             #DataFrame has D and F capitals


print(test_df.info())
test_df


# In[ ]:




