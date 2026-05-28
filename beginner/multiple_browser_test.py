from selenium import webdriver
import time #added to allow us to pause the script and see the browser actions

#Store the URLs of the website we want to visit in a list
sites = [
    "https://www.google.com", 
    "https://www.python.org", 
    "https://www.selenium.dev"
    ]
driver = webdriver.Chrome()

# loop through the list of URLs and navigate to each one, printing the title of the page
for site in sites:
    driver.get(site)
    time.sleep(2)  # Wait for the page to load but not recommended for production code, better to use explicit waits
    print(driver.title)
    
driver.quit()