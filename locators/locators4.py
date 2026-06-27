from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#locator by CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sauce")

time.sleep(3)
#locator by XPATH
driver.find_element(By.XPATH,'//input[@id="login-button"]').click()
print(driver.current_url)
time.sleep(3)
driver.quit()