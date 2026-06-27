from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# locating search input field by NAME locator and sending value "selenium" to it using send_keys() method.
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(3)
driver.find_element(By.NAME,"q").clear() # clearing the search input field
# driver.find_element(By.NAME,"btnK").click()
time.sleep(3)

# driver.find_element(By.LINK_TEXT,'https://mail.google.com/mail/?authuser=0&ogbl').click()
print(driver.title)
driver.quit()