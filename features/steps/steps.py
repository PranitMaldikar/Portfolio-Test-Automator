from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException
import os

# Load environment variables
load_dotenv()
USER_NAME = os.getenv("USER_NAME")   
PASSWORD = os.getenv("PASSWORD") 
LOGIN_URL = os.getenv("LOGIN_URL")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
DASHBOARD_URL = os.getenv("DASHBOARD_URL")

# Navigate to the login page
@given(u'the user has navigated to the login page')
def step_impl(context):
    context.driver.get(LOGIN_URL)

# Perform login with credentials
@given(u'the user logs in with valid credentials')
def step_impl(context):
    context.driver.find_element(By.NAME, "email").send_keys(USER_NAME)
    context.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    context.driver.find_element(By.ID, "rcc-confirm-button").click()
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    # Click on the Home button after login
    home_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='page-wrapper']/div[1]/nav/div[1]/div[1]/div/button"))
    )
    home_button.click()

# Placeholder for navigating to the dashboard
@given(u'the user has navigated to the dashboard')
def step_impl(context):
    pass

# Verify portfolio is visible
@then(u'the user should see their portfolio')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".m-0.p-0.slashed-zero.text-inherit.text-lg.font-medium"))
        )
        assert "Your portfolio" == element.text
    except TimeoutException:
        raise AssertionError("Portfolio element was not found within the timeout period.")

# Ensure user has a verified payment method (assumed external verification)
@given('the user has a verified payment method')
def step_impl(context):
    pass

# Search for a stock by ticker symbol
@then(u'the user searches for a stock inside \'Symbol\' field on the dashboard using the ticker symbol "AAPL"')
def step_impl(context):
    symbol_input = context.driver.find_element(By.CSS_SELECTOR, "input.styled__TextInput-sc-1j17nla-1.bcbDMU")
    symbol_input.send_keys('AAPL')

# Select order type from a dropdown
@then(u'the user selects \'Market\' in the \'Order Type\' dropdown')
def step_impl(context):
    dropdown = WebDriverWait(context.driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "ant-select-selection--single")))
    dropdown.click()
    option = WebDriverWait(context.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-dropdown')]//li[text()='Market']")))
    option.click()

# Enter quantity of stock to order
@then(u'the user enters \'2\' in the quantity field')
def step_impl(context):
    quantity_field = context.driver.find_element(By.CSS_SELECTOR, "input.ant-input.NumberInput__StyledInput-n6tlji-0.hUmVoV")
    context.driver.execute_script("arguments[0].value = '';", quantity_field)  # Clear the field using JavaScript
    quantity_field.send_keys('2')  

# Click the 'Review Order' button
@then(u'the user clicks the \'Review Order\' button')
def step_impl(context):
    review_order_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".quick-trade-temp-review-button"))
    )
    review_order_button.click()

# Confirm the order
@then(u'the user clicks the \'Confirm Order\' button')
def step_impl(context):
    confirm_order = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.buLeqt'))
    )
    confirm_order.click()

# Check for order creation confirmation
@then(u'the user should receive a confirmation saying \'Order Created\'')
def step_impl(context):
    confirmation = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-notification-notice-message"))
    )
    assert "Order Created" == confirmation.text
