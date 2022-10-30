import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():

    driver = webdriver.Chrome()
    driver.get("https://www.idntimes.com/")
    driver.implicitly_wait(10)

    # driver.find_element("xpath", "//img[@alt='IDN Times']").click()
    # print("Logo OK")

    driver.find_element("xpath", "//a[@class='btn join-btn']").click()
    print("Login/Register OK")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.find_element("xpath", "//a[@class='btn-back']").click()
    driver.implicitly_wait(10)

    driver.find_element("xpath", "//a[@href='#search-modal']").click()
    driver.find_element("xpath", "//input[@type='search']").send_keys("Korea")
    time.sleep(5)
    driver.find_element("xpath", "//button[@class='close']").click()
    print("Search OK")
    driver.implicitly_wait(10)

    driver.find_element("xpath", "//div[@class='side-headline slick-initialized slick-slider']")
    count = len(driver.find_elements("xpath", "//div[@class='slick-slide']"))
    print(count)

    driver.quit()


if __name__ == "__main__":
    main()
