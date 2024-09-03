from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from commonsteps import evaluate


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


@when('I enter "{to}" as destinatary')
def step_impl(context, to):
    context.driver.find_element(By.ID, "to").send_keys(to)


@when('I enter a message "{text}" in the message field')
def step_impl(context, text):
    context.driver.find_element(By.ID, "message").send_keys(text)


@when('I click the Send Message button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Send Message']").click()


@then('I see the message "{expected}"')
def step_impl(context, expected):
    found = ""
    try:
        context.driver.switch_to.frame(context.driver.find_element(By.ID, "messagesFrame"))
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li")))
        elements = context.driver.find_elements(By.CSS_SELECTOR, "li")
        context.driver.switch_to.default_content()
        logger.debug(elements)
        for element in elements:
            text_message = element.text
            logger.debug(text_message)
            if expected in text_message:
                found = text_message
                break
    except:
        evaluate(context.driver, found, expected)        


@when('I click the logout link')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "log out").click()
