import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():

    driver = webdriver.Chrome()
    driver.get("https://www.idntimes.com/")
    driver.implicitly_wait(10)

    if driver.find_elements("xpath", "//div[@class='header-logo']"):
        print("Logo: Passed")
    else: 
        print("Logo: Failed")

    if driver.find_elements("xpath", "//i[@class='idn-mini-icon idn-search']"):
        print("Search Button: Passed")
    else: 
        print("Search Button: Failed")
    
    if driver.find_elements("xpath", "//a[@class='btn join-btn']"):
        print("Login/Register Button: Passed")
    else: 
        print("Login/Register Button: Failed")

    if driver.find_element("xpath", "//nav[@class='header-navbar']"):
        print("Menu Bar: Passed")
    else: 
        print("Menu Bar: Failed")
    
    if driver.find_element("xpath", "//section[@id='headline']"):
        count = len(driver.find_elements("xpath", "//section[@class='wrapper-trending clearfix']//div[@class='slick-track']//div[@class='slick-slide slick-active' or @class='slick-slide slick-current slick-active']"))
        if count == 5:
            print("Headline Section: ", count, "News Passed")
    else: 
        print("Headline Section: Failed")
    
    if driver.find_element("xpath", "//section[@class='wrapper-trending clearfix']"):
        news1 = len(driver.find_elements("xpath", "//section[@class='latest-post clearfix'][1]//div[@class='list-latest main-latest clearfix'][1]//div[@class='box-latest box-list ']"))
        news2 = len(driver.find_elements("xpath", "//section[@class='latest-post clearfix'][1]//div[@class='list-latest sub-latest clearfix'][1]//div[@class='box-latest box-list ']"))
        if news1 == 2 and news2 == 16:
            print("Latest Section 18 News: Passed")
        elif news1 < 2 and news2 < 16:
            print("Latest Section News Quantity Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']"):
        count = len(driver.find_elements("xpath", "//section[@class='latest-post clearfix']"))
        if count == 6:
            print("Section Category 5 Categories: Passed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']"):
        news1 = len(driver.find_elements("xpath", "//section[@class='latest-post clearfix'][2]//div[@class='list-latest main-latest clearfix'][1]//div[@class='box-latest box-list ']"))
        news2 = len(driver.find_elements("xpath", "//section[@class='latest-post clearfix'][2]//div[@class='list-latest sub-latest clearfix'][1]//div[@class='box-latest box-list ']"))
        if news1 == 2 and news2 == 8:
            print("Section Category 10 News: Passed")
        elif news1 < 2 and news2 < 8:
            print("Section Category News Quantity Failed")

    if driver.find_elements("xpath", "//footer[@class='static-footer']"):
        print("Footer: Passed")
    else: 
        print("Footer: Failed")

    driver.quit()


if __name__ == "__main__":
    main()
