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
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
read = driver.find_element_by_css_selector("[data-product_id='181']")
read.click()
element = driver.find_element_by_css_selector("[itemprop='name']")
element_get_text = element.text
if element_get_text == "HTML5 Forms":
    print("заголовок книги назвается HTML5 Forms")
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
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
html = driver.find_element_by_link_text("HTML")
html.click()
count_products = driver.find_elements_by_css_selector("[rel='nofollow']")
if len(count_products) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка")
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
selector = driver.find_element_by_css_selector("[value='menu_order']")
selector_selected=selector.get_attribute("selected")
if selector is not None:
    print("вариант сортировки выбран по умолчанию")
sorting = driver.find_element_by_css_selector("[value='price']").click()
high = driver.find_element_by_css_selector("[value='price']")
high_selected=high.get_attribute("selected")
if high is not None:
    print("вариант сортировки по цене от большей к меньшей")
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
my = driver.find_element_by_link_text("My Account")
my.click()
email_address = driver.find_element_by_id("username")
email_address.send_keys("Kira750@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Kirasam2023")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
android_btn = driver.find_element_by_css_selector("[data-product_id='169']")
android_btn.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_old_price_text == "₹600.00"
assert book_new_price_text == "₹450.00"
book_cover = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()
book_cover_close = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
my = driver.find_element_by_link_text("My Account")
my.click()
email_address = driver.find_element_by_id("username")
email_address.send_keys("Kira750@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Kirasam2023")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
mastering_btn = driver.find_element_by_css_selector("[data-product_id='165']")
mastering_btn.click()
time.sleep(5)
quantity = driver.find_element_by_css_selector("[class='cartcontents']")
quantity_text = quantity.text
price = driver.find_element_by_css_selector("#wpmenucartli > a > span:nth-child(3)")
price_text = price.text
assert quantity_text == "1 Item"
assert price_text == "₹350.00"
basket = driver.find_element_by_css_selector("[class='wpmenucart-icon-shopping-cart-0']")
basket.click()
subtotal = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "350"))
total = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong > span"), "357"))
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
my = driver.find_element_by_link_text("My Account")
my.click()
email_address = driver.find_element_by_id("username")
email_address.send_keys("Kira750@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Kirasam2023")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
mastering_btn = driver.find_element_by_css_selector("[data-product_id='165']")
mastering_btn.click()
time.sleep(5)
basket = driver.find_element_by_css_selector("[class='wpmenucart-icon-shopping-cart-0']")
basket.click()
btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')))
btn.click()
first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Kiril")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Иванов")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("79115034789")
selector = driver.find_element_by_class_name("select2-arrow")
selector.click()
field = driver.find_element_by_id("s2id_autogen1_search")
field.send_keys("Russia")
word = driver.find_element_by_class_name("select2-match")
word.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Lenina,25")
town = driver.find_element_by_id("billing_city")
town.send_keys("Moskow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
post = driver.find_element_by_id("billing_postcode")
post.send_keys("105043")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
option = driver.find_element_by_css_selector("[value='cheque']")
option.click()
order_btn = driver.find_element_by_id("place_order")
order_btn.click()
some_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
payment = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details > tfoot > tr:nth-child(3)"), "Check Payments"))
driver.quit()
