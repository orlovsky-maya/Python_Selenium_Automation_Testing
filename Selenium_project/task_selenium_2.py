from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import *
import time
from selenium.webdriver import ActionChains, Keys


# # The syntax to run the script on Ubuntu OS
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--remote-debugging-port=9515")
# browser = webdriver.Chrome(options=chrome_options)

# The syntax to run the script on Windows OS
browser = webdriver.Chrome()

link = 'https://demoqa.com/date-picker'

try:
    # Open browser and go to the link
    browser.implicitly_wait(2)
    browser.get(link)

    # Find select date field and click it
    select_date_field = browser.find_element(By.ID, 'datePickerMonthYearInput')
    select_date_field.click()

    # Get current date
    current_date = datetime.today()
    print('Current_date:', current_date)

    # Get future_date and time
    future_date = current_date + timedelta(days=10)
    print('Future date:', future_date)

    # Get future_date string
    future_date_str = future_date.strftime('%m/%d/%Y')
    print('Future date string:', future_date_str)

    # Clear select date field
    for i in range(10):
        select_date_field.send_keys(Keys.BACKSPACE)
    print('Cleared')

    # Input future date to select date field
    select_date_field.send_keys(future_date_str)
    select_date_field.send_keys(Keys.RETURN)
    print('Finish')


finally:
    time.sleep(2)
    browser.quit()


# Incorrect solution(need to be updated)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from datetime import *
# import time
#
# # The syntax to run the script on Ubuntu OS
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--remote-debugging-port=9515")
# browser = webdriver.Chrome(options=chrome_options)
#
# # # The syntax to run the script on Windows OS
# # browser = webdriver.Chrome()
#
# link = 'https://demoqa.com/date-picker'
#
# try:
#     # Open browser and go to the link
#     browser.implicitly_wait(5)
#     browser.get(link)
#
#     # Find select date field and click it
#     select_date_field = browser.find_element(By.ID, 'datePickerMonthYearInput')
#     select_date_field.click()
#
#     # Get current date
#     current_date = datetime.now()
#     print(current_date)
#
#     # Get future_date
#     future_date = current_date + timedelta(days=20)
#     print(future_date)
#
#     # Divide future date
#     day_of_week = future_date.strftime('%A')
#     month = future_date.strftime('%B')
#     day = future_date.strftime('%d')
#     year = future_date.strftime('%Y')
#     print(day_of_week, month, day, year)
#
#     # Conditions adding end
#     if int(day) % 10 == 1:
#         end = 'st'
#     elif int(day) % 10 == 2:
#         end = 'nd'
#     elif int(day) % 10 == 3:
#         end = 'rd'
#     else:
#         end = 'th'
#
#     # Find locator for future date and click it
#     locator = f'[aria-label="Choose {day_of_week}, {month} {int(day)}{end}, {year}"]'
#     new_date = browser.find_element(By.CSS_SELECTOR, locator)
#     new_date.click()
#     print('Future date is selected')
#
# finally:
#     time.sleep(3)
#     browser.quit()



