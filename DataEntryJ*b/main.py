import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://forms.gle/eqySHxXu9DhSjANC9")

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
chars_to_addr= " \n\',"
chars_to_price="+/mo"
soup = BeautifulSoup(response.text,"html.parser")

property_address =soup.find_all('address',attrs={'data-test':'property-card-addr'})
address = [n.text.strip(chars_to_addr).replace("|", "").replace(",", "") for n in property_address]
total_address = len(address)

property_price = soup.find_all('span',attrs={'data-test':'property-card-price'})
price = [n.text.strip(chars_to_price).replace(",","").replace("+ 1 bd","").replace("+ 1bd","") for n in property_price]

property_link = soup.find_all('a',attrs={'data-test':'property-card-link'})
link = [n.get("href") for n in property_link]

for i in range(total_address):

    address_input = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'input[aria-labelledby="i1 i4"]'))
    )
    address_input.click()
    time.sleep(1)
    address_input.send_keys(str(address[i]))

    price_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[aria-labelledby="i6 i9"]'))
    )
    price_input.click()
    time.sleep(1)
    price_input.send_keys(str(price[i]))

    link_to_home_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[aria-labelledby="i11 i14"]'))
    )
    link_to_home_input.click()
    time.sleep(1)
    link_to_home_input.send_keys(str(link[i]))

    submit = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'))
    )
    submit.click()

    another = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
    )

    another.click()