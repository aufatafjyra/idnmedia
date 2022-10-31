import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():

    driver = webdriver.Chrome()
    driver.get("https://www.idntimes.com/")
    driver.implicitly_wait(10)

    if driver.find_elements("xpath", "//div[@class='header-logo']"):
        print("Logo Passed")
    else: 
        print("Logo Failed")

    if driver.find_elements("xpath", "//i[@class='idn-mini-icon idn-search']"):
        print("Search Button Passed")
    else: 
        print("Search Button Failed")
    
    if driver.find_elements("xpath", "//a[@class='btn join-btn']"):
        print("Login/Register Button Passed")
    else: 
        print("Login/Register Button Failed")

    if driver.find_element("xpath", "//nav[@class='header-navbar']"):
        print("Menu Bar Passed")
    else: 
        print("Menu Bar Failed")
    
    if driver.find_element("xpath", "//section[@id='headline']"):
        print("Headline Section Passed")
    else: 
        print("Headline Section Failed")
    
    if driver.find_element("xpath", "//section[@class='wrapper-trending clearfix']"):
        print("Trending Section Passed")
    else: 
        print("Trending Section Failed")
    
    if driver.find_element("xpath", "//div[@class='left-content']"):
        print("Latest Section Passed")
    else: 
        print("Latest Section Failed")
    
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

    # driver.find_element("xpath", "//img[@alt='IDN Times']").click()
    # print("Logo OK")

    # driver.find_element("xpath", "//a[@class='btn join-btn']").click()
    # print("Login/Register OK")
    # driver.implicitly_wait(10)
    # time.sleep(5)
    # driver.find_element("xpath", "//a[@class='btn-back']").click()
    # driver.implicitly_wait(10)

    # driver.find_element("xpath", "//a[@href='#search-modal']").click()
    # time.sleep(5)
    # driver.find_element("xpath", "//input[@type='search']").send_keys("Korea")
    # time.sleep(5)
    # driver.find_element("xpath", "//button[@class='close']").click()
    # print("Search OK")
    # driver.implicitly_wait(10)

    # driver.find_element("xpath", "//section[@id='headline']")
    # count = len(driver.find_elements("xpath", "//div[@class='slick-slide']"))
    # print(count)

    driver.quit()


if __name__ == "__main__":
    main()
