from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Scrape NASA 

def NASA():
    browser = init_browser()
    news = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news["news_title"] = soup.find("a", class_="content-title").get_text()
    news["news_p"] = soup.find( class_="article_teaser_body").get_text()

    return news

# Scrape JPL

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def JPL():
    browser = init_browser()
    images = {}

    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    browser.visit(featured_image_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    images["img"] = soup.find("a", class_="result-title").get_text()
    images["link"] = soup.find("span", class_="result-price").get_text()

    return images

# Scrape Mars Facts

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def Mars():
    browser = init_browser()
    facts = {}

    mars_facts_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    browser.visit(mars_facts_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    facts["equatorial_diameter"] = soup.find("a", class_="result-title").get_text()
    facts["polar_diameter"] = soup.find("span", class_="result-price").get_text()
    facts["mass"] = soup.find("a", class_="result-title").get_text()
    facts["moons"] = soup.find("span", class_="result-price").get_text()
    facts["orbit_distance"] = soup.find("a", class_="result-title").get_text()
    facts["surface_temperature"] = soup.find("span", class_="result-price").get_text()
    facts["first_record"] = soup.find("a", class_="result-title").get_text()
    facts["recorded_by"] = soup.find("span", class_="result-price").get_text()


    return facts


# Scrape Mars Hemipheres

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def Hemispheres():
    browser = init_browser()
    hemispheres = {}

    mars_hem_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    browser.visit(mars_hem_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    hemispheres["title"] = soup.find("a", class_="itemLink.product-item").get_text()
    hemispheres["img_url"] = soup.find("img", class_="thumb").get_text()

    return hemispheres
