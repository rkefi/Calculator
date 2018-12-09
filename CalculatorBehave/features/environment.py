# Defining the Tests Setup and Teardown methods

from selenium import webdriver
from browser import Browser
from pages.calculator_page import CalculatorPage, CalculatorPageLocator

def before_all(context):
    # Defining the test setup
    context.browser = Browser()
    context.calculator_page = CalculatorPage()
    context.calculator_page_locators = CalculatorPageLocator()

def after_all(context):
    # Defining the test teardown
    context.browser.close()
