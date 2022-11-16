from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("Selenium WebDriver")
print("Click on the search button")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
print(driver.current_url)
driver.close()