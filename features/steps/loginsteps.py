from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I launch the Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'I go to the home page')
def step_impl(context):
    context.driver.get("http://serverlx:8090")


@then(u'I am redirected to the login page')
def step_impl(context):
    url = context.driver.current_url
    print(f"login page: {url}")
    assert url == 'http://serverlx:8090/login'


@then(u'I can see the \'Simple Chat\' title at the top')
def step_impl(context):
    title = context.driver.find_element(By.TAG_NAME, "h1").text
    assert title == 'Simple Chat'


@when('I provide a valid "{username}" and "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when(u'I provide a valid username')
def step_impl(context):
    username = 'John'
    context.driver.find_element(By.ID, "username").send_keys(username)


@when(u'I provide a valid password')
def step_impl(context):
    password = 'password'
    context.driver.find_element(By.ID, "password").send_keys(password)


@when(u'I click the Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I am redirected to the chat room page')
def step_impl(context):
    url = context.driver.current_url
    print(url)
    assert url == 'http://serverlx:8090/room'


@then(u'I close Chrome browser')
def step_impl(context):
    context.driver.close()


@when(u'I provide an invalid password')
def step_impl(context):
    wrong_password = 'wrong_password'
    context.driver.find_element(By.ID, "password").send_keys(wrong_password)


@when(u'I provide an invalid username')
def step_impl(context):
    invalid_username = 'invalid_username'
    context.driver.find_element(By.ID, "username").send_keys(invalid_username)


@then(u'I get \'Invalid username or password\'')
def step_impl(context):
    text = context.driver.find_element(By.TAG_NAME, "pre").text
    assert text == 'Invalid username or password'