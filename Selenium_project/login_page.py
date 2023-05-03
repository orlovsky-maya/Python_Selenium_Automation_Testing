from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The syntax to run the script on Ubuntu OS
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")


class Login_page:

    def __init__(self, browser):
        self.browser = browser

    def authorization(self, login_name, login_password):
        # Find and fill in username and password fields
        user_name_field = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, 'user-name')))
        user_name_field.send_keys(login_name)

        password_field = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, 'password')))
        password_field.send_keys(login_password)

        # Find Login button on page and click it
        login_button = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
        # print(f'{login_name} is logged in')
