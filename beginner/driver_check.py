from selenium import webdriver

driver  = webdriver.Chrome()  #Create a new instance of the Chrome driver
driver.get("https://www.python.org") #Navigate to the Python website
print("Title:", driver.title)  #Print the title of the page to confirm it loaded correctly
driver.quit()