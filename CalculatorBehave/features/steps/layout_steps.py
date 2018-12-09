# Layout feature steps definition

from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_true

@step('I navigate to the Calculator  page')
def step_impl(context):
    context.calculator_page.navigate("http://jsbin.com/hudape/1/")

@step('The Calculator main page is displayed')
def step_impl(context):
    assert_equal(context.calculator_page.get_page_title(), "JS Bin")

@step('Ten numeric buttons should be visible and enabled')
def step_impl(context):
    for i in range(0,10):
        assert_true(context.calculator_page.element_is_visible(By.XPATH,"//button[@value="+str(i)+"]"))
        assert_true(context.calculator_page.element_is_enabled(By.XPATH,"//button[@value="+str(i)+"]"))
        
@step('Operations buttons should be visible and enabled')
def step_impl(context):
    assert_true(context.calculator_page.operations_buttons_visible_enabled())
    
@step('I see an expression and result display')
def step_impl(context):
    assert_true(context.calculator_page.expression_output_visible())
    
@step('The expression and output fields are empty')
def step_impl(context):
    assert_equal(context.calculator_page.get_expression_display_value(),'')
    assert_equal(context.calculator_page.get_output_display_value(),'')

