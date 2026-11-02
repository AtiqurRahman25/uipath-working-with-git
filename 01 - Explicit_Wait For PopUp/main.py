# Md. Atiqur Rahman Sifat
# RPA - Robotic Process Automation Intern

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Access a browser
    driver.get("https://practice-automation.com/ads/")

    # Explicit Wait - Wait for 10 seconds.
    wait = WebDriverWait(driver, )

    # Explicit Wait - Wait unitil elements' explicit visiblility
    heading = wait.until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div"))
    )
    print("Page loaded successfully, heading is:", heading.text)

finally:
    driver.quit()