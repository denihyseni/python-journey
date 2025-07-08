from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

start_time = datetime.datetime.now()
difference = datetime.timedelta(minutes=5)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor")

grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma")

factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory")

mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine")

shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment")

alchemy_lab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')

portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal")

time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')




while True:
    try:
        cookie.click()
        money = driver.find_element(By.CSS_SELECTOR, value="#money")
        cursor_cost = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b ")
        text = cursor_cost.text
        cost = int(text.strip("Cursor - ").replace(",", ""))

        grandma_cost = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b ")
        text1 = grandma_cost.text
        grandmas_price = int(text1.strip("Grandma - ").replace(",", ""))

        factory_cost = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b ")
        text2 = factory_cost.text
        factory_prices = int(text2.strip("Factory - ").replace(",", ""))

        mine_cost = driver.find_element(By.CSS_SELECTOR, value="#buyMine b ")
        text3 = mine_cost.text
        mines_price = int(text3.strip("Mine - ").replace(",", ""))

        Shipment_cost = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b ")
        text4 = Shipment_cost.text
        shipment_prices = int(text4.strip("Shipment - ").replace(",", ""))

        alchemy_lab_cost = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
        text5 = alchemy_lab_cost.text
        al_cost = int(text5.strip("Alchemy lab - ").replace(",", ""))

        portal_cost = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b ")
        text6 = portal_cost.text
        p_cost = int(text6.strip("Portal - ").replace(",", ""))

        time_machine_cost = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
        text7 = time_machine_cost.text
        tm_cost = int(text7.strip("Time machine - ").replace(",", ""))



        if int(money.text) > cost:
            cursor.click()


        elif int(money.text) > grandmas_price:
            grandma.click()

        elif int(money.text) > factory_prices:
            factory.click()

        elif int(money.text) > mines_price:
            mine.click()

        elif int(money.text) > shipment_prices:
            shipment.click()

        elif int(money.text) > al_cost:
            alchemy_lab.click()

        elif int(money.text) > p_cost:
            portal.click()

        elif int(money.text) > tm_cost:
            time_machine.click()

        current = datetime.datetime.now()
        if current - start_time >= difference:
            driver.quit()
            break
        time.sleep(0.1)
    except Exception as e:
        print(f"A error has occurred: {e}")
        driver.quit()
        break


