#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page. Searching for elements with a specific combination of tag (div) and attribute (list_text). As an example, ul.item_list would be found in HTML as <ul class="item_list">.
#Secondly, we're also telling our browser to wait one second before searching for components. The optional delay is useful because sometimes dynamic pages take a little while to load, especially if they are image-heavy.
browser.is_element_present_by_css('div.list_text', wait_time=10)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
# . is used for selecting classes, such as list_text. code 'div.list_text' pinpoints the <div /> tag with the class of list_text.
# when using select_one, the first matching element returned will be a <li /> element with a class of slide and all nested elements within it.
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


# <div class="content_title">A New Video Captures the Science of NASA's Perseverance Mars Rover</div>
# <div class="article_teaser_body">With a targeted launch date of July 30, the next robotic scientist NASA is sending to the to the Red Planet has big ambitions.</div>


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


slide_elem.find('div', class_='content_title').text


# In[ ]:


# Use the parent element to find the first `div` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the first `div` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='article_teaser_body').get_text()
news_title


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list. Then, it turns the table into a 
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


browser.quit()


# # Challenge code

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[6]:


print(slide_elem)


# In[7]:


slide_elem.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[13]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[15]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[16]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[17]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[93]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[100]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[42]:


# Parse the resulting html with soup
#html = browser.html
#img_soup = soup(html, 'html.parser')
#img_soup


# In[68]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
#hemisphere_image_urls_rel = img_soup.find_all('a', class_='item')
#print(hemisphere_image_urls_rel)


# In[95]:


#get sample link
#hemisphere_image_urls_link = hemisphere_image_urls_rel[0]['href']
#print(f'https://astrogeology.usgs.gov/{hemisphere_image_urls_link}')
#img_url = 'https://astrogeology.usgs.gov/'+hemisphere_image_urls_link
#browser.visit(img_url)
#browser.back()
#print(image_urls_link)


# In[96]:


#get sample title
#hemisphere_image_urls_title = hemisphere_image_urls_rel[0].find('img', class_='thumb description-thumb').get('alt')
#print(hemisphere_image_urls_title)


# In[101]:


#hemisphere_image_urls = [{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov//search/map/Mars/Viking/cerberus_enhanced'}]
#for i in range(len(hemisphere_image_urls_rel)):
#    print(i)    
#    my_dict = {}
#    hemisphere_image_urls_link = 'https://astrogeology.usgs.gov/'+hemisphere_image_urls_rel[i]['href']
#    my_dict["title"]=hemisphere_image_urls_rel[0].find('img', class_='thumb description-thumb').get('alt')
#    browser.visit(hemisphere_image_urls_link)
#    html = browser.html
#    img_soup = soup(html, 'html.parser')
#    image_urls_link = img_soup.find('a', target_='_blank')['href']
#    my_dict["img_url"]=image_urls_link
#    hemisphere_image_urls.append(my_dict)
#print(hemisphere_image_urls)

for image_count in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[image_count].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[102]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls 


# In[103]:


# 5. Quit the browser
browser.quit()


# In[ ]:




