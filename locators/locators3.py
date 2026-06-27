from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)

driver.find_element(By.LINK_TEXT,'About').click()
print(driver.title)
driver.find_element(By.PARTIAL_LINK_TEXT,'See for').click()
time.sleep(3)
print(driver.title)
driver.quit()