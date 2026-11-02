from selenium import webdriver
import time

# Openning on Microsoft Edge
driver = webdriver.Edge()
driver.get("https://www.google.com")

# Wait for website preparation
driver.implicitly_wait(2)

# Collecting title info
websiteTitle = driver.title

if "Google" in websiteTitle:
    print(f"[Log info] - {websiteTitle} opened successfully.")
else:
    print(f"Unexpected page opened.")

time.sleep(3)

# print(websiteTitle)