import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def initialization ():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    inner_driver = webdriver.Chrome(options=chrome_options)
    inner_driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return inner_driver

driver = initialization()

cookie = driver.find_element(By.ID, value="cookie")
five_min = time.time() + 60*1
time_to_buy = time.time() + 5

while True:

    cookie.click()
    if time.time() > time_to_buy:
        items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

        for item in reversed(items):

            if item.get_attribute("class") != "grayed":

                item.click()
                time_to_buy = time.time() + 5
                break

    if time.time() > five_min :
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

driver.quit()