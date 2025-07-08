import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("")
email = "pejeya1900@dlbazi.com"
password = "siemens"
phone_number = "+12345677367"

time.sleep(3)

x = driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/button')
x.click()
time.sleep(3)
initial_click = driver.find_element(By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
initial_click.click()

time.sleep(1)

email_entry = driver.find_element(By.ID,value="username")
email_entry.click()
email_entry.send_keys(f"{email}")

time.sleep(5)

password_entry = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]' ))
)
password_entry.click()
password_entry.send_keys("s")
password_entry.click()
password_entry.send_keys("iem")
password_entry.click()
password_entry.send_keys("ens")

time.sleep(5)

sign_in = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[4]/button')
sign_in.click()

time.sleep(1)
#
# job_application = WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-view-name='job-card']"))
# )
# applied_count = 0
# total_jobs = len(job_application)
# print(total_jobs)
#
#
# for i in range(total_jobs):
#     try:
#         job = job_application[i]
#         driver.execute_script("arguments[0].scrollIntoView(true)")
#
#         try:
#             apply_button_element = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.XPATH, '//*[@id="jobs-apply-button-id"]'))
#             )
#             apply_button_span = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'span'))
#             )
#             if "Easy Apply" in apply_button_element.text:
#                 WebDriverWait(driver, 5).until(EC.element_to_be_clickable(job)).click()  # Wait for job to be clickable
#                 apply_easy = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.XPATH, '//*[@id="jobs-apply-button-id"]'))
#                 )
#                 apply_easy.click()
#             else:
#                 continue
#
#             try:
#
#
#                 job_window = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="-1"]')
#                 if job_window.get_attribute('class') == 'mt3':
#                     print(f"{i + 1} job has been applied to")
#                     submit_button = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable(
#                             (By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
#                         )
#                     )
#                     submit_button.click()
#
#                     # Initialize and wait for exit_out_app *here*, inside the modal context
#                     exit_out_app = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss"]'))
#                     )
#                     exit_out_app.click()
#
#                     done_button = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located(
#                             (
#                                 By.CSS_SELECTOR,
#                                 'button[data-view-name="seeker-next-best-action-card-cta-with-impression"]',
#                             )
#                         )
#                     )
#                     done_button.click()
#
#                 else:
#                     time.sleep(3)
#                     driver.back()
#
#
#             except StaleElementReferenceException as sere:
#                 print(f"Object changed {sere}")
#                 # time.sleep(random.uniform(1,3))  # Remove this time.sleep()
#                 exit_out_saveapp = WebDriverWait(driver, 5).until(
#                     EC.element_to_be_clickable(
#                         (
#                             By.CSS_SELECTOR,
#                             'button[data-control-name="discard_application_confirm_btn"]',
#                         )
#                     )
#                 )
#                 exit_out_saveapp.click()
#                 continue
#             except TimeoutException as toe:
#                 print(f"Timeout Exception: {toe} during application process")
#                 continue # Add this to handle timeouts in the inner try
#         except NoSuchElementException as nsee:
#             print(f"No such element found {nsee}")
#             # time.sleep(random.uniform(1,3))  # Remove this time.sleep()
#
#             exit_out_app = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss"]'))
#                 )
#             exit_out_app.click()
#             continue
#         except TimeoutException as toe:
#             print(f"Timeout Exception: {toe} during job click or Easy Apply")
#             continue # Add this to handle timeouts in the outer try
#     except IndexError as e:
#         print(f"List out of range {e}")
#         break
#
#
# print(nsee)
# print(toe)
# print(e)



