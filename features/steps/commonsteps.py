from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def evaluate(driver, got, expected):
    print(f"Got: {got}")
    try:
        assert got == expected
    except:
        driver.close()
        assert False, f"Expected: `{expected}`, but got `{got}`. Test FAILED."


@given('I launch the Chrome browser')
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(3)


@when('I go to the home page')
def step_impl(context):
    context.driver.get("http://localhost:8090")


@then('I can see the Simple Chat title at the top')
def step_impl(context):
    expected = 'Simple Chat'
    title = context.driver.find_element(By.TAG_NAME, "h1").text
    evaluate(context.driver, title, expected)


@then('I am redirected to the login page')
def step_impl(context):
    expected = 'http://localhost:8090/login'
    url = context.driver.current_url
    evaluate(context.driver, url, expected)


@then('I am redirected to the chat room page')
def step_impl(context):
    expected = 'http://localhost:8090/room'
    # WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(By.TAG_NAME, "h2"))
    url = context.driver.current_url
    evaluate(context.driver, url, expected)


@when('I click the Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()
