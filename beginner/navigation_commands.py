from selenium import webdriver  
import time # for learning pusrpose only not recommended in real projects


#launch browser - create an active session of browser having a uniques session Id or instance ID
driver = webdriver.Chrome() # driver is a variable here which is storing the reference of the active session of browser

# navigate to url for this we use get() method of webdriver class and pass the url as argument
driver.get("https://www.google.com/")

time.sleep(3) # for learning pusrpose only so that we can visualize the browser and its actions, not recommended in real projects

# navigate to another url
driver.get("https://www.facebook.com/")
time.sleep(3) 

# navigate back to previous url
driver.back() # back() method is used to navigate back to the previous url that means it will take us back to google.com
time.sleep(3)

# navigate forward to next url
driver.forward() # forward() method is used to navigate forward to the next url that means it will take us forward to facebook.com
time.sleep(3)

# refresh the current page
driver.refresh() # refresh() method is used to refresh the current page
time.sleep(3)

# close the current window
driver.close() # close() method is used to close the current window opened by the webdriver
time.sleep(3)


# quit the browser - close all the windows opened by the webdriver
driver.quit() # quit() method is used to close all the windows opened by the webdriver and end the session