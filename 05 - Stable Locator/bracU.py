from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.bracu.ac.bd/")
driver.implicitly_wait(10)

textinput = driver.find_element(By.LINK_TEXT, "Students").click()
driver.implicitly_wait(10)

cloudFlare = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Verify you are human']").click()
driver.implicitly_wait(10)

time.sleep(20)

driver.quit()