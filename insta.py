from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

browser = webdriver.Firefox() # Get local session of firefox

browser.implicitly_wait(0.5)
browser.get("https://www.instagram.com/explore/tags/royalenfieldcolombia/")
a=browser.find_elements_by_xpath("//a[starts-with(@href, /explore)]")
print(a)
for element in a:
    print(element.get_attribute('href'))