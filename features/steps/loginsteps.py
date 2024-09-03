from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch the Chrome browser')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options)


@when('I go to the home page')
def step_impl(context):
    context.driver.get("http://serverlx:8090")


@then('I am redirected to the login page')
def step_impl(context):
    url = context.driver.current_url
    print(f"login page: {url}")
    assert url == 'http://serverlx:8090/login'


@then('I can see the \'Simple Chat\' title at the top')
def step_impl(context):
    title = context.driver.find_element(By.TAG_NAME, "h1").text
    assert title == 'Simple Chat'


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


@when('I click the Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then('I am redirected to the chat room page')
def step_impl(context):
    url = context.driver.current_url
    print(url)
    assert url == 'http://serverlx:8090/room'


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
    text = context.driver.find_element(By.TAG_NAME, "pre").text
    assert text == 'Invalid username or password'