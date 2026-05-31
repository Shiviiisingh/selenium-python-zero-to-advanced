from selenium import webdriver # importing the webdriver module from the selenium package
import time

driver = webdriver.Chrome() # creating a new instance of the Chrome driver
driver.get("https://www.google.com") # navigating to the Google homepage
time.sleep(3) # waiting for 3 seconds to allow the page to load

driver.maximize_window() # maximizing the browser window
time.sleep(2) # waiting for 2 seconds to see the effect of maximizing the window

driver.minimize_window() # minimizing the browser window
time.sleep(2) # waiting for 2 seconds to see the effect of minimizing the window

driver.maximize_window()
driver.refresh() # refreshing the current page
time.sleep(2) # waiting for 2 seconds to see the effect of refreshing the page

driver.quit() # closing the browser and ending the WebDriver session