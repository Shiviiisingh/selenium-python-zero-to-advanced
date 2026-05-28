from selenium import webdriver
import time


print("Step 1: Python script is running...")
print("Step 2 & 3: Selenium WebDriver connecting to ChromeDriver...")

driver = webdriver.Chrome()

print("Step 4: Chrome Browser created successfully!")


driver.get("https://www.google.com")
print(f"Successfully navigated to: {driver.title}")
    
time.sleep(3)
    
print("Cleaning up: Closing Chrome and terminating ChromeDriver.")
driver.quit()



