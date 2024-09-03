from behave import *
from selenium.webdriver.common.by import By

from commonsteps import evaluate


@when('I provide a valid "{username}" and "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when('I provide a valid username "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.ID, "username").send_keys(username)


@when('I provide a valid password')
def step_impl(context):
    password = 'password'
    context.driver.find_element(By.ID, "password").send_keys(password)


@then('I close Chrome browser')
def step_impl(context):
    context.driver.close()


@when('I provide an invalid password')
def step_impl(context):
    wrong_password = 'wrong_password'
    context.driver.find_element(By.ID, "password").send_keys(wrong_password)


@when('I provide an invalid username')
def step_impl(context):
    invalid_username = 'invalid_username'
    context.driver.find_element(By.ID, "username").send_keys(invalid_username)


@then('I get \'Invalid username or password\'')
def step_impl(context):
    expected = 'Invalid username or password'
    text = context.driver.find_element(By.TAG_NAME, "pre").text
    evaluate(context.driver, text, expected)
