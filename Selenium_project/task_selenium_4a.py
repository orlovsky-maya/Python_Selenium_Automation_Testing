from selenium import webdriver
from selenium import common
from login_page import *

# The syntax to run the script on Ubuntu OS

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")
browser = webdriver.Chrome(options=chrome_options)

# # The syntax to run the script on Windows OS
# browser = webdriver.Chrome()

# Open browser
link = 'https://www.saucedemo.com/'
browser.get(link)

# Test data
users_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'


# Log out from account
def log_out():
    burger_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(((By.ID,
                                                                                       'react-burger-menu-btn'))))
    burger_button.click()

    logout_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(((By.ID,
                                                                                       'logout_sidebar_link'))))
    logout_button.click()


# Checking that the user is valid
for user in users_list:
    login = Login_page(browser)
    login.authorization(user, password)

    try:
        # Find Products text on Products page and compare
        title_text = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                       '#header_container .title')))
        title_value = title_text.text
        assert title_value == 'Products', 'Incorrect title on Products page'

        print(f'{user}: PASS')
        log_out()

    except common.exceptions.TimeoutException:
        browser.refresh()
        print(f'{user}: FAIL')