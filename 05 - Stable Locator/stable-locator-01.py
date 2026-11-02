from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.implicitly_wait(2)

websiteTitle = driver.title
print(f"[Log Info] - {websiteTitle} opened successfully!")

driver.find_element(By.ID, "my-text-id").send_keys("Md. Atiqur Rahman Sifat")
driver.find_element(By.NAME, "my-password").send_keys("SifatNasimurSararNahif")
driver.find_element(By.NAME, "my-textarea").send_keys("N/A")
driver.find_element(By.ID, "my-radio-2").click()
driver.save_screenshot("entireWindow.png")

time.sleep(2)

driver.quit()