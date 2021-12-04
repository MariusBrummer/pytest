import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

TACOAPP_HOME = 'https://tacos.nl/'

# Scenarios

scenarios('../features/notStopping.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('It is the start of the day')
def start_of_day(browser):
    browser.get(TACOAPP_HOME)


# When Steps

@when('I buy fresh supplies')
def buy_fresh_supplies(browser, phrase):
    pass


# Then Steps

@then('I have to buy supplies for 100 tacos')
def supply_amount_100(browser, phrase):
    pass
