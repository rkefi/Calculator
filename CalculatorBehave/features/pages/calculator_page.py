from selenium.webdriver.common.by import By
from browser import Browser

class CalculatorPageLocator(object):
    # Calculator  Page Objects Locators

    DELETE_BUTON = (By.XPATH, "//button[text()='DEL']")
    EQ_BUTTON = (By.XPATH,"//button[text()='EQ']")
    PLUS_BUTTON =  (By.XPATH,"//button[text()='PLUS']")
    MINUS_BUTTON = (By.XPATH,"//button[text()='MINUS']")
    MULT_BUTTON = (By.XPATH,"//button[text()='MULT']")
    DIV_BUTTON = (By.XPATH,"//button[text()='DIV']")
    EXPRESSION_INPUT = (By.ID,"expression")
    OUTPUT_DISPLAY = (By.ID, "output")
    
    OPERATION_BUTTONS = [DELETE_BUTON, EQ_BUTTON, PLUS_BUTTON, MINUS_BUTTON, MULT_BUTTON, DIV_BUTTON]


class CalculatorPage(Browser):
    # Calculator Page Methods

    def navigate(self, address):
        self.driver.get(address)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def element_is_visible(self, *locator):
        return self.driver.find_element(*locator).is_displayed()
        
    def element_is_enabled(self, *locator):
        return self.driver.find_element(*locator).is_enabled()

    def get_page_title(self):
        return self.driver.title
    
    def get_expression_display_value(self):
        return self.driver.find_elements(By.CLASS_NAME,"display")[0].text
    
    def get_output_display_value(self):
        return self.driver.find_elements(By.CLASS_NAME,"display")[1].text
    
    def operations_buttons_visible_enabled(self):
        for operation in CalculatorPageLocator.OPERATION_BUTTONS:
            state = (self.element_is_visible(*operation) and self.element_is_enabled(*operation))
        return state
    
    def expression_output_visible(self):
        return (self.element_is_visible(*CalculatorPageLocator.EXPRESSION_INPUT) and self.element_is_visible(*CalculatorPageLocator.OUTPUT_DISPLAY))
            
            
        
        
