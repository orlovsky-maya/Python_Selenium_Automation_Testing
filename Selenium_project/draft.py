# from datetime import datetime
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# import time
#
# # import unittest
# chrome_options = Options()
# chrome_options.add_argument("--remote-debugging-port=9515")
# browser = webdriver.Chrome(options=chrome_options)
#
# link = 'https://www.saucedemo.com/'
#
# user = 'standard_user'
# password = 'secret_sauce'
#
# try:
#     # Open browser and go to the link
#     browser.implicitly_wait(5)
#     browser.get(link)
#
#     """Login page"""
#
#     # Find and fill in username and password fields
#     user_name_field = browser.find_element(By.ID, 'user-names')
#     user_name_field.send_keys(user)
# #
# #     password_field = browser.find_element(By.ID, 'password')
# #     password_field.send_keys(password)
# #
# #     # Find Login button on page and click it
# #     login_button = browser.find_element(By.ID, 'login-button')
# #     login_button.click()
# #     print('GOOD Login page')
# finally:
#     time.sleep(2)
#
#
# from selenium.common import NoSuchElementException
# try:
#     element = browser.find_element(By.METOD, SELECTOR)
#     element.click()
# except NoSuchElementException as exception:
#     Example actions:
#     time.sleep(10)
#     browser.refresh()
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((METOD, SELOCTOR)))
# button.click()
