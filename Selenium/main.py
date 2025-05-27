from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID,value="submit")
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# # print(link.text)

# bg_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')


event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name":event_names[n].text
    }
print(events)

driver.quit()