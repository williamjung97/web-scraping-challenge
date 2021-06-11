#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager


# In[131]:

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data = {}

# In[4]:


# NASA News Url
    url = ('https://redplanetscience.com/')
    browser.visit(url)
# Making the HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    slide_elem = soup.select_one('div.list_text')
    slide_elem.find('div', class_='content_title')


# In[5]:


    # Extracting Title
    nasa_title = slide_elem.find('div',class_='content_title').get_text()


    # In[6]:


    # Extracting Paragraph
    nasa_paragraph = slide_elem.find('div',class_='article_teaser_body').get_text()


# In[7]:

    mars_data['nasa_title'] = nasa_title
    mars_data['nasa_paragraph'] = nasa_paragraph
    # Collecting the Latest News Title and Paragraph
    print(nasa_title)
    print(nasa_paragraph)


# In[8]:


    #Nasa's JPL Mars Space Url
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    # Making the HTML 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_url = soup.find('img',class_='headerimage fade-in')['src']

    featured_image_url = 'https://spaceimages-mars.com/' + image_url
    print(featured_image_url)

    mars_data['featured_image_url'] = featured_image_url


    # In[9]:


    #Mars Facts webpage
    mars_facts = 'https://galaxyfacts-mars.com/'
    mars_facts_table = pd.read_html(mars_facts)

    mars_facts_table[0]


    # In[10]:


    # Creating Dataframe 
    df = mars_facts_table[0]
    header_row = 0
    df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    df = df.drop(header_row)
    df


    # In[11]:


    # Converting Dataframe to HTML
    html_table = df.to_html()
    html_table


    # In[12]:


    # Clean up unwanted newlines
    html_table.replace('\n','')

    mars_data['html_table'] = html_table

    # In[133]:


    #Mars Hemisphere Url
    mars_hemi_url = "https://marshemispheres.com/"
    browser.visit(mars_hemi_url)


# In[134]:


    hemisphere_urls = [
        'https://marshemispheres.com/cerberus.html',
        'https://marshemispheres.com/schiaparelli.html',
        'https://marshemispheres.com/syrtis.html',
        'https://marshemispheres.com/valles.html'
    ]

# Create Empty Dictionary
    hemisphere_image_urls = []


# In[135]:


# For loop through urls
    for url in hemisphere_urls:
        print(url)
        links={}
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # Get Titles
        mars_title = soup.find('h2', class_ = 'title').get_text()
        # Get urls for the img
        mars_links = soup.find('img', class_='wide-image')['src']
        img_url = mars_hemi_url + mars_links
        links = dict({'title': mars_title, 'img_url': img_url})
        hemisphere_image_urls.append(links)

        browser.back()


# In[136]:


    hemisphere_image_urls

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls


# In[130]:


    browser.quit()


# In[ ]:

    return mars_data


