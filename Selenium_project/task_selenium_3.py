from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from locators_mod import *


# The syntax to run the script on Ubuntu OS
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")

class Product:
    """Create Product class"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductLocators:
    """Create Product locators class"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    """Find selected product and price on Products page"""

    def get_product(self):
        product_name = browser.find_element(By.CSS_SELECTOR, self.name)
        product_name_value = product_name.text

        product_price = browser.find_element(By.CSS_SELECTOR, self.price)
        product_price_value = product_price.text

        product = Product(product_name_value, product_price_value)

        return product


class CatalogLocators:
    """Create Catalog locators class"""

    def __init__(self, product, button):
        self.product = product
        self.button = button


"""General data"""

link = 'https://www.saucedemo.com/'
user = 'standard_user'
password = 'secret_sauce'

"""Create catalog locators variables"""

backpack_loc = CatalogLocators(ProductLocators(backpack_name, backpack_price), backpack_add_button)
bike_light_loc = CatalogLocators(ProductLocators(bike_light_name, bike_light_price), bike_light_add_button)
bolt_t_shirt_loc = CatalogLocators(ProductLocators(bolt_t_shirt_name, bolt_t_shirt_price), bolt_t_shirt_add_button)
fleece_jacket_loc = CatalogLocators(ProductLocators(fleece_jacket_name, fleece_jacket_price), fleece_jacket_add_button)
onesie_loc = CatalogLocators(ProductLocators(onesie_name, onesie_price), onesie_add_button)
t_shirt_red_loc = CatalogLocators(ProductLocators(t_shirt_red_name, t_shirt_red_price), t_shirt_red_add_button)

"""User greeting and product selection """

print('Приветствую тебя в нашем интернет магазине')
print('Выберите один из следующих товаров и укажите его номер:\n'
      '1 - Sauce Labs Backpack\n'
      '2 - Sauce Labs Bike Light\n'
      '3 - Sauce Labs Bolt T-Shirt\n'
      '4 - Sauce Labs Fleece Jacket\n'
      '5 - Sauce Labs Onesie\n'
      '6 - Test.allTheThings() T-Shirt (Red)')

"""Create catalog locators dictionary"""

catalog_locators_dic = {'1': backpack_loc,
                        '2': bike_light_loc,
                        '3': bolt_t_shirt_loc,
                        '4': fleece_jacket_loc,
                        '5': onesie_loc,
                        '6': t_shirt_red_loc}

"""Input number of product"""
catalog_number = input()
while catalog_number not in ['1', '2', '3', '4', '5', '6']:
    print('You input incorrect symbol. Please try again.(correct numbers from 1 to 6)')
    catalog_number = input()

"""Select catalog locator in catalog locators dictionary"""
catalog_locator = catalog_locators_dic[catalog_number]

"""Go through the test"""

try:

    # Open browser and go to the link

    # # The syntax to run the script on Windows OS
    # browser = webdriver.Chrome()

    # The syntax to run the script on Ubuntu OS
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(link)
    browser.implicitly_wait(5)

    """Login page"""

    # Find and fill in username and password fields
    user_name_field = browser.find_element(By.ID, 'user-name')
    user_name_field.send_keys(user)

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Find Login button on page and click it
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    print('Finish Login page')

    """Catalog page"""

    # Get name and price selected product
    catalog_product = catalog_locator.product.get_product()
    name_product = catalog_product.name
    price_product = catalog_product.price
    print('Selected product on catalog page: ', name_product, price_product)

    # Add selected product to the cart
    add_to_cart_button = browser.find_element(By.ID, catalog_locator.button)
    add_to_cart_button.click()
    print('Product is added to the cart')

    # Find the cart button and click it
    cart_button = browser.find_element(By.CSS_SELECTOR, cart_button_loc)
    cart_button.click()
    print('The cart is opened')

    """Cart page"""
    # Find selected product and price on Cart page and compare
    cart_product = ProductLocators(name_cart, price_cart).get_product()
    print('Selected product on cart page: ', cart_product.name, cart_product.price)
    assert name_product == cart_product.name, 'Names of products are different'
    assert price_product == cart_product.price, 'Prices of products are different'

    # Scroll to the Checkout button
    action = ActionChains(browser)
    checkout_button = browser.find_element(By.ID, checkout_button_loc)
    action.move_to_element(checkout_button).perform()
    checkout_button.click()
    print('Finish Cart page')

    """Checkout: Your Information page"""

    # Find and fill in First name, Last name and Zip Code fields
    first_name_field = browser.find_element(By.ID, 'first-name')
    first_name_field.send_keys('Maya')

    last_name_field = browser.find_element(By.ID, 'last-name')
    last_name_field.send_keys('Orlovskaya')

    zip_code_field = browser.find_element(By.ID, 'postal-code')
    zip_code_field.send_keys('1234')

    # Scroll to Continue button
    action = ActionChains(browser)
    continue_button = browser.find_element(By.ID, 'continue')
    action.move_to_element(continue_button).perform()
    continue_button.click()
    print('Finish Checkout: Your Information page')

    """Checkout: Overview page"""

    # Find selected product and price on Overview page and compare
    overview_product = ProductLocators(name_overview, price_overview).get_product()
    print('Selected product on Overview page: ', overview_product.name, overview_product.price)
    assert name_product == overview_product.name, 'Names of products are different'
    assert price_product == overview_product.price, 'Prices of products are different'

    # Scroll to the Item total and find Item total on Overview page and compare
    action = ActionChains(browser)
    item_total = browser.find_element(By.CSS_SELECTOR, item_total_loc)
    action.move_to_element(item_total).perform()
    item_total_value_on_page = item_total.text
    assert item_total_value_on_page == f'Item total: {price_product}', 'Product amount does not match'

    # Scroll to Finish button
    action = ActionChains(browser)
    continue_button = browser.find_element(By.ID, 'finish')
    action.move_to_element(continue_button).perform()
    continue_button.click()
    print('Finish Overview page')

    """Finish page"""
    # Find finish message and compare
    finish_message = browser.find_element(By.CSS_SELECTOR, 'h2.complete-header')
    finish_message_value = finish_message.text
    correct_message = 'Thank you for your order!'
    assert finish_message_value == correct_message, "Finish message isn't correct"
    print("Finish Test")

finally:
    time.sleep(1)
browser.quit()
