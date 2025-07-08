from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import datetime
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"
AUTOMATION_DURATION_MINUTES = 5
REFRESH_INTERVAL_SECONDS = 0.1

def initialize_driver():
    """Initializes the Chrome WebDriver with specified options."""
    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open after script finishes
    driver = webdriver.Chrome(options=options)
    driver.get(GAME_URL)
    logging.info(f"Opened game URL: {GAME_URL}")
    return driver

def get_element(driver, by, value):
    """Safely retrieves a single WebElement."""
    try:
        return driver.find_element(by, value)
    except NoSuchElementException:
        logging.error(f"Element not found: {by}={value}")
        return None

def get_elements(driver, by, value):
    """Safely retrieves multiple WebElements."""
    try:
        return driver.find_elements(by, value)
    except NoSuchElementException:
        logging.error(f"Elements not found: {by}={value}")
        return []

def get_money(driver):
    """Retrieves the current amount of cookies."""
    money_element = get_element(driver, By.CSS_SELECTOR, "#money")
    return int(money_element.text.replace(",", "")) if money_element else 0

def get_upgrade_price(driver, upgrade_selector):
    """Retrieves the price of an upgrade."""
    price_element = get_element(driver, By.CSS_SELECTOR, f"{upgrade_selector} b")
    return int(price_element.text.replace(",", "")) if price_element else float('inf')

def click_cookie(driver):
    """Clicks the main cookie."""
    cookie_button = get_element(driver, By.CSS_SELECTOR, "#cookie")
    if cookie_button:
        try:
            cookie_button.click()
        except StaleElementReferenceException:
            logging.warning("Cookie element became stale, attempting to find again.")
            click_cookie(driver) # Recursive call to retry
    else:
        logging.error("Main cookie button not found.")

def buy_upgrade(driver, upgrade_selector, upgrade_name, current_money):
    """Attempts to buy an upgrade if affordable."""
    upgrade_button = get_element(driver, By.CSS_SELECTOR, upgrade_selector)
    if upgrade_button and upgrade_button.is_enabled():
        price = get_upgrade_price(driver, upgrade_selector)
        if current_money > price:
            try:
                upgrade_button.click()
                logging.info(f"Bought {upgrade_name} for {price} cookies.")
                return True
            except StaleElementReferenceException:
                logging.warning(f"{upgrade_name} button became stale, will attempt to find again.")
    return False

def main():
    """Main function to run the Cookie Clicker bot."""
    driver = initialize_driver()
    start_time = datetime.datetime.now()
    duration = datetime.timedelta(minutes=AUTOMATION_DURATION_MINUTES)

    upgrade_selectors = {
        "Cursor": "#buyCursor",
        "Grandma": "#buyGrandma",
        "Factory": "#buyFactory",
        "Mine": "#buyMine",
        "Shipment": "#buyShipment",
        "Alchemy lab": '//*[@id="buyAlchemy lab"]',
        "Portal": "#buyPortal",
        "Time machine": '//*[@id="buyTime machine"]'
    }

    while True:
        try:
            click_cookie(driver)
            current_money = get_money(driver)

            # Attempt to buy upgrades in a prioritized order
            buy_upgrade(driver, upgrade_selectors["Cursor"], "Cursor", current_money)
            buy_upgrade(driver, upgrade_selectors["Grandma"], "Grandma", current_money)
            buy_upgrade(driver, upgrade_selectors["Factory"], "Factory", current_money)
            buy_upgrade(driver, upgrade_selectors["Mine"], "Mine", current_money)
            buy_upgrade(driver, upgrade_selectors["Shipment"], "Shipment", current_money)
            buy_upgrade(driver, upgrade_selectors["Alchemy lab"], "Alchemy lab", current_money)
            buy_upgrade(driver, upgrade_selectors["Portal"], "Portal", current_money)
            buy_upgrade(driver, upgrade_selectors["Time machine"], "Time machine", current_money)

            elapsed_time = datetime.datetime.now() - start_time
            if elapsed_time >= duration:
                logging.info(f"Automation duration of {AUTOMATION_DURATION_MINUTES} minutes reached. Quitting.")
                driver.quit()
                break

            time.sleep(REFRESH_INTERVAL_SECONDS)

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            driver.quit()
            break

if __name__ == "__main__":
    main()