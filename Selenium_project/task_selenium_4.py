from selenium import webdriver
from selenium import common
from datetime import datetime
from login_page import *

# The syntax to run the script on Ubuntu OS

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")
browser = webdriver.Chrome(options=chrome_options)

# # The syntax to run the script on Windows OS
# browser = webdriver.Chrome()


link = 'https://www.saucedemo.com/'
browser.get(link)


# Log out from account
def log_out(user_name):
    burger_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(((By.ID,
                                                                                       'react-burger-menu-btn'))))
    burger_button.click()

    logout_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(((By.ID,
                                                                                       'logout_sidebar_link'))))
    logout_button.click()
    # print(f'{user_name} is logged out')


# Checking that the user is valid
class ValidUserTes:
    description = 'Valid User Test:'

    def test_check(self):
        # Find link on image on Products page and compare
        product_image = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                          '#item_4_img_link '
                                                                                          '.inventory_item_img')))
        product_image_link = product_image.get_attribute('src')
        assert product_image_link == 'https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg', \
            'Incorrect image on Products page'


# Checking that the user is locked
class LockedUserTes:
    description = 'Locked User Test:'

    def test_check(self):
        # Find link error message on Login page and compare
        error_message = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
        error_message_value = error_message.text
        assert error_message_value == 'Epic sadface: Sorry, this user has been locked out.', \
            'Incorrect error message'


valid_user = ValidUserTes()
locked_user = LockedUserTes()

users_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'
tests_list = [valid_user, locked_user]

for test in tests_list:
    print(test.description)

    for user in users_list:
        login = Login_page(browser)

        try:
            # Checking for a time delay after clicking on the login button
            start_time = datetime.utcnow()
            login.authorization(user, password)
            end_time = datetime.utcnow()
            delta = (end_time - start_time).total_seconds()
            assert delta < 4.0
            test.test_check()
            print(f'{user}: PASS')
        except AssertionError:
            print(f'{user}: FAILED')
        except common.exceptions.TimeoutException:
            print(f'{user}: FAILED')
        finally:
            current_url = browser.current_url
            if current_url == 'https://www.saucedemo.com/':
                browser.refresh()
            else:
                log_out(user)
    print()