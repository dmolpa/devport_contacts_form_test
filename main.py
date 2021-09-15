import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from contacts_page_xpath_selectors import first_name_input_selector, last_name_input_selector, email_input_selector, phone_number_input_selector, message_text_area_selector, submit_button_selector

browser = webdriver.Firefox()

browser.get('about:blank')
browser.set_window_size(1920, 1200)
browser.get("https://devport.io/ua/contact")

class contactsPageTest(unittest.TestCase):
       
    
    
    def test_first_name_input(self):
        new_value = "first_name"
        timeout = 2
        
        element_present = EC.presence_of_element_located((By.XPATH, first_name_input_selector))
        WebDriverWait(browser, timeout).until(element_present)

        element = browser.find_element_by_xpath(first_name_input_selector)
        element.send_keys(new_value)
        self.assertEqual(element.get_attribute("value"), new_value)
        
    def test_last_name_input(self):
        new_value = "last_name"

        element = browser.find_element_by_xpath(last_name_input_selector)
        element.send_keys(new_value)
        self.assertEqual(element.get_attribute("value"), new_value)
        
    def test_email_input(self):
        new_value = "some@email.com"

        element = browser.find_element_by_xpath(email_input_selector)
        element.send_keys(new_value)
        self.assertEqual(element.get_attribute("value"), new_value)
        
    def test_phone_num_input(self):
        new_value = "5555555"

        element = browser.find_element_by_xpath(phone_number_input_selector)
        element.send_keys(new_value)
        self.assertEqual(element.get_attribute("value"), new_value)
        
    def test_message_text_area(self):
        new_value = "This is a dummy message"
        
        element = browser.find_element_by_xpath(message_text_area_selector)
        element.send_keys(new_value)
        self.assertEqual(element.get_attribute("value"), new_value)
        
    def test_form_submit(self):
        element = browser.find_element_by_xpath(submit_button_selector)
        self.assertEqual(element.is_enabled(), True)
    
    @classmethod
    def tearDownClass(self):
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
