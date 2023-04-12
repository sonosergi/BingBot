# BingBot
A python script that automates images scraping and downloading using Selenium an Bing Image Search.

Run the script from the command line with the search query as an argument. If no argument is provided, the script will prompt the user to enter a search query.

'''bash
python image_scraper.py [search_query]
'''

The script will open a Chrome browser, navigate to Bing's image search page, enter the search query, extract the links to the images, write them to a JSON file, create a directory to store the downloaded images and download the images to that directory.
Dependencies

    Selenium
    ChromeDriver
    Webdriver-Manager
    wget

You can install the required dependencies by running:

'''bash
pip install -r requirements.txt
'''

Note

This script is intended for educational purposes only. It is not intended to violate the terms of use of any website or service.
Bing Image Search API

Bing offers a search API that allows developers to search for images, among other types of content. The API provides a more efficient and reliable way to search for images than scraping Bing's image search page.

To use the API, you need to sign up for a Microsoft Azure account and create a Bing Search resource. You can then use the API key provided by the resource to send search requests to the API and receive JSON responses with the search results.

Using the Bing Image Search API instead of scraping Bing's image search page has several advantages, such as:

    Better performance and reliability.
    More customization options, such as filtering by image type, size, and color.
    Compliance with Bing's terms of use and API terms of use.

However, using the API also has some limitations, such as:

    Limited number of requests per month, depending on the pricing tier of your Bing Search resource.
    Need to handle authentication and rate limiting.
    Need to parse JSON responses instead of HTML pages.

If you decide to use the Bing Image Search API in your project, you can find more information and documentation on the Bing Search API v7 website.
