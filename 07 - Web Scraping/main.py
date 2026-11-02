from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import time

def popUp_elimination():
    close_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/a"))
    )
    close_btn.click()
    print(f"[Log Message] - Pop Up Closed!")

try:
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.thedailystar.net/news/crime-justice")
        driver.implicitly_wait(2)
        print(f"[Log Message] - {driver.title} opened successfully!")

        popUp_elimination()

        # search_element = driver.find_element((By.XPATH, "/html/body/div[2]/header/div/div/div/div[3]/a[2]/svg[1]/path")).click()
        # search_element.send_keys("Crime" + Keys.ENTER)
    except WebDriverException as e:
        print(f"Error to open the website.")
        print(f"Details: {e}")
finally:
    driver.quit()