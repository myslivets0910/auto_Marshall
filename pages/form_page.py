import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        #first_name = 'Pedro'
        #last_name = 'Pasckal'
        #email = 'hello@world.com'
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        self.element_is_visible(Locators.CURRENT_ADRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.element_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        # result_text = []
        # for i in result_list:
        #  result_text.append(i.text)
        return result_text

   # time.sleep(10)