from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
# import time - Always not the best solution

try:
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.amazon.com/")
        time.sleep(5)
        print(f"[Log Info] - '{driver.title}' opened successfully!")

        # Typing Input
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Protein Powder")
        driver.find_element(By.ID, "nav-search-submit-button").click()

        driver.save_screenshot("Amazon.png")

        # Choosing Element
        xpath = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div[3]/div[1]/a/h2/span"
        card = driver.find_element(By.XPATH, xpath)
        print(card.text)

    except WebDriverException as e:
        print(f"Erron to open the website.")
        print(f"Details: {e}")
finally:
    driver.quit()