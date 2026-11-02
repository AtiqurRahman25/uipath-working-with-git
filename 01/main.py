from selenium import webdriver
import time

driver = webdriver.Chrome()

# Access a browser
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(5)
driver.quit()