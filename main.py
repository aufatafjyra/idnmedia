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
        print("Headline Section: Passed")
    else: 
        print("Headline Section: Failed")
    
    if driver.find_element("xpath", "//section[@class='wrapper-trending clearfix']"):
        count = len(driver.find_elements("xpath", "//section[@class='wrapper-trending clearfix']//div[@class='slick-track']//div[@class='slick-slide slick-active' or @class='slick-slide slick-current slick-active']"))
        if count == 5:
            print("Trending Section: ", count, "News Passed")
    
    if driver.find_element("xpath", "//section[@class='latest-post clearfix']//span[text()='Berita Terkini']"):
        count = len(driver.find_element("xpath", "//section[@class='//section[@class='latest-post clearfix'][1]//div[@class='list-latest main-latest clearfix' or @class='list-latest sub-latest clearfix']"))
        print("Latest Section ", count, " News: Passed")
    else: 
        print("Latest Section News: Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']//span[text()='News']"):
        print("Section Category 1 Passed")
    else: 
        print("Section Category 1 Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']//span[text()='Hype']"):
        print("Section Category 2 Passed")
    else: 
        print("Section Category 2 Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']//span[text()='Life']"):
        print("Section Category 3 Passed")
    else: 
        print("Section Category 3 Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']//span[text()='Men']"):
        print("Section Category 4 Passed")
    else: 
        print("Section Category 4 Failed")
    
    if driver.find_elements("xpath", "//section[@class='latest-post clearfix']//span[text()='Science']"):
        print("Section Category 5 Passed")
    else: 
        print("Section Category 5 Failed")
    
    if driver.find_elements("xpath", "//footer[@class='static-footer']"):
        print("Footer Passed")
    else: 
        print("Footer Failed")

    driver.quit()


if __name__ == "__main__":
    main()
