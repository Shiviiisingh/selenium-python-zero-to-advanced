from selenium import webdriver

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
    print(driver.title)
    
driver.quit()