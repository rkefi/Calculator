# Operations feature steps definition

from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_true

    
@step(u'I enter a single digit number {single_digit:d}')
def step_impl(context, single_digit):
    context.calculator_page.click_element(By.XPATH,"//button[@value="+str(single_digit)+"]")
    
@step(u'I enter a multiple digit number {multi_digit:d}')
def step_impl(context, multi_digit):
    for digit in str(multi_digit):
        context.calculator_page.click_element(By.XPATH,"//button[@value="+digit+"]")
    
@step(u'I choose an arithmetic operation "{arith_operation}"')
def step_impl(context, arith_operation):
    context.calculator_page.click_element(By.XPATH,"//button[text()='"+arith_operation+"']")
    
@step('The output display remains empty')
def step_impl(context):
    assert_equal(context.calculator_page.get_output_display_value(),'')
    
@step('The Output Displays "{expected}"')
def step_impl(context,expected):
    assert_equal(context.calculator_page.get_output_display_value(),expected)
    
@step('I evaluate my expression')
def step_impl(context):
    context.calculator_page.click_element(*context.calculator_page_locators.EQ_BUTTON)
    
@step('I press the delete button')
def step_impl(context):
    context.calculator_page.click_element(*context.calculator_page_locators.DELETE_BUTON)
    
@step(u'Only My Last Input Is Deleted {expected_result:d}')
def step_impl(context, expected_result):
    expected_value = str(expected_result)
    assert_equal(context.calculator_page.get_output_display_value(),expected_value)
    
@step(u'The output display is updated with the result of the evaluation of my expression {expected_result:d}')
def step_impl(context,expected_result):
    assert_equal(context.calculator_page.get_output_display_value(),str(expected_result))
    