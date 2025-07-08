from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,value="fName")
first_name.click()
first_name.send_keys("Deni")

last_name = driver.find_element(By.NAME,value="lName")
last_name.click()
last_name.send_keys("Hyseni")

email_input = driver.find_element(By.NAME,value="email")
email_input.click()
email_input.send_keys("deni.hyseni@gmail.com")

button = driver.find_element(By.CSS_SELECTOR,value="button")
button.click()

# all_portals.click()


