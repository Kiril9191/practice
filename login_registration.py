import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my = driver.find_element_by_link_text("My Account")
my.click()
email_address = driver.find_element_by_id("reg_email")
email_address.send_keys("Kira750@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("Kirasam2023")
register_btn = driver.find_element_by_name("register")
register_btn.click()
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my = driver.find_element_by_link_text("My Account")
my.click()
email_address = driver.find_element_by_id("username")
email_address.send_keys("Kira750@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Kirasam2023")
login_btn = driver.find_element_by_name("login")
login_btn.click()
element = driver.find_element_by_link_text("Logout")
element_get_text = element.text
assert element_get_text == "Logout"
driver.quit()
