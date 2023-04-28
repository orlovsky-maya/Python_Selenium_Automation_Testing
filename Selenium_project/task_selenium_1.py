from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# # The syntax to run the script on Ubuntu OS
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--remote-debugging-port=9515")
# browser = webdriver.Chrome(options=chrome_options)

# The syntax to run the script on Windows OS
browser = webdriver.Chrome()

link = 'https://www.saucedemo.com/'

user = 'standard_user'
password = 'secret_sauce'

try:
    # Open browser and go to the link
    browser.implicitly_wait(5)
    browser.get(link)

    """Login page"""

    # Find and fill in username and password fields
    user_name_field = browser.find_element(By.ID, 'user-name')
    user_name_field.send_keys(user)

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Find Login button on page and click it
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    print('GOOD Login page')

    """Products page"""

    # Find product_1 and price on Products page and add to cart
    product_1_products_page = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link .inventory_item_name')
    name_product_1_products_page = product_1_products_page.text

    price_product_1_products_page = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(1) > '
                                                                          'div:nth-child(2) > div:nth-child(2) > '
                                                                          'div:nth-child(1)')
    price_product_1_value_products_page = price_product_1_products_page.text

    add_to_cart_button_product_1 = browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_button_product_1.click()

    # Find product_2 and price on Products page and add to cart
    product_2_products_page = browser.find_element(By.CSS_SELECTOR, '#item_0_title_link .inventory_item_name')
    name_product_2_products_page = product_2_products_page.text

    print('GOOD Products page')

    price_product_2_products_page = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item:nth-child(2)>'
                                                                          'div:nth-child(2)>div:nth-child(2)>'
                                                                          'div:nth-child(1)')
    price_product_2_value_products_page = price_product_2_products_page.text

    add_to_cart_button_product_2 = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_to_cart_button_product_2.click()

    # Find the cart button and click it
    cart_button = browser.find_element(By.CSS_SELECTOR, 'span.shopping_cart_badge')
    cart_button.click()

    """Cart page"""

    # Find product_1 and price on Cart page and compare
    product_1_cart_page = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link .inventory_item_name')
    name_product_1_cart_page = product_1_cart_page.text
    assert name_product_1_products_page == name_product_1_cart_page, 'Names of products are different'

    price_product_1_cart_page = browser.find_element(By.CSS_SELECTOR, '#cart_contents_container>div>.cart_list>'
                                                                      'div:nth-child(3)>div:nth-child(2)>'
                                                                      'div:nth-child(3)>div')
    price_product_1_value_cart_page = price_product_1_cart_page.text
    assert price_product_1_value_products_page == price_product_1_value_cart_page, 'Prices of products are different'

    # Scroll to the product_2 and price on Cart page and compare
    action = ActionChains(browser)
    product_2_cart_page = browser.find_element(By.CSS_SELECTOR, '#item_0_title_link .inventory_item_name')
    action.move_to_element(product_2_cart_page).perform()
    name_product_2_cart_page = product_2_cart_page.text
    assert name_product_2_products_page == name_product_2_cart_page, 'Names of products are different'

    price_product_2_cart_page = browser.find_element(By.CSS_SELECTOR, '#cart_contents_container>div>.cart_list>'
                                                                      'div:nth-child(4)>div:nth-child(2)>'
                                                                      'div:nth-child(3)>div')
    price_product_2_value_cart_page = price_product_2_cart_page.text
    assert price_product_2_value_products_page == price_product_2_value_cart_page, 'Prices of products are different'

    # Scroll to the Checkout button
    action = ActionChains(browser)
    checkout_button = browser.find_element(By.ID, 'checkout')
    action.move_to_element(checkout_button).perform()
    checkout_button.click()
    print('GOOD Cart page')

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
    print('GOOD Checkout: Your Information page')

    """Checkout: Overview page"""

    # Find product_1 and price on Overview page and compare
    product_1_overview_page = browser.find_element(By.CSS_SELECTOR, '#item_4_title_link .inventory_item_name')
    name_product_1_overview_page = product_1_overview_page.text
    assert name_product_1_products_page == name_product_1_overview_page, 'Names of products are different'

    price_product_1_overview_page = browser.find_element(By.CSS_SELECTOR, '#checkout_summary_container>div>.cart_list>'
                                                                          'div:nth-child(3)>.cart_item_label>'
                                                                          '.item_pricebar>div')
    price_product_1_value_overview_page = price_product_1_overview_page.text
    price_product_1_value_overview_page_num = float(price_product_1_value_overview_page[1:])
    assert price_product_1_value_products_page == price_product_1_value_overview_page, 'Prices of products are '

    # Scroll to the product_2 and find product_2 and price on Overview page and compare
    action = ActionChains(browser)
    product_2_overview_page = browser.find_element(By.CSS_SELECTOR, '#item_0_title_link .inventory_item_name')
    action.move_to_element(product_2_overview_page).perform()
    name_product_2_overview_page = product_2_overview_page.text
    assert name_product_2_products_page == name_product_2_overview_page, 'Names of products are different'

    price_product_2_overview_page = browser.find_element(By.CSS_SELECTOR, '#checkout_summary_container>div>.cart_list>'
                                                                          'div:nth-child(4)>.cart_item_label>'
                                                                          '.item_pricebar>div')
    price_product_2_value_overview_page = price_product_2_overview_page.text
    price_product_2_value_overview_page_num = float(price_product_2_value_overview_page[1:])
    assert price_product_2_value_products_page == price_product_2_value_overview_page, 'Prices of products ' \
                                                                                       'are different'

    # Scroll to the Item total and find Item total on Overview page
    action = ActionChains(browser)
    item_total = browser.find_element(By.CSS_SELECTOR, '.summary_info .summary_subtotal_label')
    action.move_to_element(item_total).perform()
    item_total_value_on_page = item_total.text

    # Calculate the amount
    summa = price_product_1_value_overview_page_num + price_product_2_value_overview_page_num
    item_total_with_summa = f'Item total: ${summa}'
    assert item_total_value_on_page == item_total_with_summa, 'Product amount does not match'
    print('GOOD Checkout: Checkout: Overview page')
finally:
    time.sleep(2)
    browser.quit()
