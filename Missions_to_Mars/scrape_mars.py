from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'C:/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info(): 
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

        # Scrape page into Soup
    html = browser.html
    soup= bs(html, "html.parser")
    
    article_heading_list = []
    
    for article_heading in soup.find_all('div',class_="content_title"):
        article_heading_list.append(article_heading.find('a').text)
        
    article_details_list = []

    for article_details in soup.find_all('div',class_="article_teaser_body"):
            
        article_details_list.append(article_details.text)

    news_title = article_heading_list[0]
    news_p = article_details_list[0]
    relative_image_path = soup.find_all('img')[2]["src"]
    featured_image_url = url + relative_image_path

    News_dict = {
        "featured_image_url": featured_image_url,
        "news_title": news_title,
        "news_p": news_p
    }

    browser.quit()

    return News_dict