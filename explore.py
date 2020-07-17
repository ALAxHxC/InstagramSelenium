from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def login(webdriver):
    # Open the instagram login page
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    # sleep for 3 seconds to prevent issues with the server
    time.sleep(3)
    # Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys('daniel1945_o@hotmail.com')
    password = webdriver.find_element_by_name('password')
    password.send_keys('Aida72584')
    # Get the login button
    try:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')
    # sleep again
    time.sleep(2)
    # click login
    button_login.click()
    time.sleep(3)
    # In case you get a popup after logging in, press not now.
    # If not, then just return
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        return


def like_photo(driver, hashtag):
    # driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(2)

    # gathering photos
    pic_hrefs = []
    for i in range(1, 7):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                             if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            # print("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            continue

    # Liking photos
    unique_photos = len(pic_hrefs)
    for pic_href in pic_hrefs:
        driver.get(pic_href)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            time.sleep(random.randint(2, 4))
            like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
            like_button().click()
            for second in reversed(range(0, random.randint(18, 28))):
                print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                      + " | Sleeping " + str(second))
                time.sleep(1)
        except Exception as e:
            time.sleep(2)
        unique_photos -= 1


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
hashtags = ['terene', 'africatwin']

login(driver)
tag = random.choice(hashtags)
like_photo(driver, tag)
