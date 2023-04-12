#!/usr/bin/env python3
import time
import sys
import os
import urllib.request
import json
import requests

# Import necessary modules from Selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Prompt user for search query if not provided as command-line argument
if len(sys.argv) < 2:
    query = input('Enter search query for images: ')
else:
    query = sys.argv[1]

# Set up options for Chrome driver
options = ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0')
options.add_argument('-incognito')

# Install and set up Chrome driver with the options
driver_path = ChromeDriverManager().install()
service = ChromeService(executable_path=driver_path)
driver = Chrome(service=service, options=options)
driver.implicitly_wait(3)

# Maximize the browser window and navigate to Bing's image search page
driver.maximize_window()
driver.get('https://www.bing.com/images/details/%7B0%7D')

# Find the search bar element and enter the search query
search_bar = driver.find_element('xpath', '//*[@id="sb_form_q"]')
time.sleep(2)
search_bar.clear()
search_bar.send_keys(query)

# Click the search button
search = driver.find_element('xpath', '//*[@id="sb_form_go"]')
search.click()

# Scroll down to load more images and extract the links to the images
n_scrolls = 4
img_links = []
for i in range(n_scrolls):
    links = driver.find_elements('xpath', '//*[@id="mmComponent_images_2"]/ul[1]/li[4]/div/div[1]/a')
    for link in links:
        time.sleep(1)
        url = link.get_attribute('href')
        if '/images/' in url:
            img_links.append(url)
            if len(img_links) >= 10:
                break
    else:
        # If we haven't found 10 links yet, scroll down and wait for more to load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

# Write the image links to a JSON file
with open('image_links.json', 'w') as f:
    json.dump(img_links, f)

# Create a directory to store the downloaded images
path = os.getcwd()
path = os.path.join(path, query)
os.mkdir(path)

# Download the images using the links extracted earlier
for idx, image in enumerate(img_links):
    save_as = os.path.join(path, query + str(idx) + '.jpg')
    response = requests.get(image)
    with open(save_as, 'wb') as f:
    	f.write(response.content)

# Close the Chrome driver
driver.quit()
