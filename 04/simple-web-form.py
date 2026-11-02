from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(f"[Log Message] - '{title}' Openned Successfully!")
textInput = driver.find_element(By.ID, "my-text-id")
textInput.send_keys("Md. Atiqur Rahman Sifat")

time.sleep(2)
driver.quit()