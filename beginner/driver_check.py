from selenium import webdriver
import time

driver  = webdriver.Chrome()
driver.get("https://www.python.org")
print("Title:", driver.title)
driver.quit()