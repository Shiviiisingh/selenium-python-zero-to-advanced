from selenium import webdriver

import time

driver = webdriver.Chrome() # creating a new instance of the Chrome driver
driver.get("https://www.google.com") # navigating to the Google homepage
time.sleep(3) # waiting for 3 seconds to allow the page to load

driver.execute_script("window.open('https://www.facebook.com');") # opening a new tab with Facebook
time.sleep(3) # waiting for 3 seconds to allow the new tab to load


# printing the list of window handles 
#window handles are unique identifiers for each open window or tab in the browser.
#window_handles is a property of the WebDriver that returns a list of all the window handles currently open in the browser.
print(driver.window_handles)

driver.close() # closing the current tab (Facebook)
time.sleep(2) # waiting for 2 seconds to see the effect of closing the tab

driver.quit() # closing the browser and ending the WebDriver session