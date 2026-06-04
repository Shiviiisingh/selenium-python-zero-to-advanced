from selenium import webdriver 
# webdriver is a module in the Selenium library that provides a way to automate web browsers. 

from selenium.webdriver.common.by import By
# By is a class that provides various methods to locate elements on a web page, such as by ID, name, class name, etc. In this code, we will use By.ID to locate the username input field on the login page of the Sauce Demo website.
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/") #using get() method to navigate on sauce demo website.
time.sleep(2)
driver.maximize_window() 
time.sleep(2)

#find_element() method is used to locate a single element on the webpage.
#find_elements() method is used to locate multiple elements on the webpage and returns a list of WebElement objects.
#send_keys() method is used to simulate typing into an input field or textarea element. It takes a string argument that represents the text to be entered into the field.
#click() method is used to simulate a mouse click on an element, such as a button or a link. It does not take any arguments and simply triggers the click event on the specified element.

#locating username input field  by ID locator  and sending value "standard_user" to it using send_keys() method.
driver.find_element(By.ID, "user-name").send_keys("standard_user") 
driver.find_element(By.ID, "password").send_keys("secret_sauce")

#locating login button by CLASS_NAME locator and clicking on it using click() method.
driver.find_element(By.CLASS_NAME, "submit-button").click()

 
driver.quit()