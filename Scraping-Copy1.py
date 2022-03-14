#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt


# In[23]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page. Searching for elements with a specific combination of tag (div) and attribute (list_text). As an example, ul.item_list would be found in HTML as <ul class="item_list">.
#Secondly, we're also telling our browser to wait one second before searching for components. The optional delay is useful because sometimes dynamic pages take a little while to load, especially if they are image-heavy.
browser.is_element_present_by_css('div.list_text', wait_time=10)


# In[9]:


html = browser.html
news_soup = soup(html, 'html.parser')
# . is used for selecting classes, such as list_text. code 'div.list_text' pinpoints the <div /> tag with the class of list_text.
# when using select_one, the first matching element returned will be a <li /> element with a class of slide and all nested elements within it.
slide_elem = news_soup.select_one('div.list_text')


# In[10]:


# <div class="content_title">A New Video Captures the Science of NASA's Perseverance Mars Rover</div>
# <div class="article_teaser_body">With a targeted launch date of July 30, the next robotic scientist NASA is sending to the to the Red Planet has big ambitions.</div>


# In[14]:


slide_elem.find('div', class_='content_title')


# In[15]:


slide_elem.find('div', class_='content_title').text


# In[16]:


# Use the parent element to find the first `div` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[17]:


# Use the parent element to find the first `div` tag and save it as `news_title`
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_P



# ### Featured Images

# In[24]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[26]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[29]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[30]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[32]:


# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list. Then, it turns the table into a 
DataFramedf = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[33]:


df.to_html()


# In[34]:


browser.quit()


# In[ ]:




