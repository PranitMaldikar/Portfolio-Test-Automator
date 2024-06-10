from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

LOGIN_URL = os.getenv("LOGIN_URL")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

def before_all(context):
    service = Service(executable_path=CHROMEDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()