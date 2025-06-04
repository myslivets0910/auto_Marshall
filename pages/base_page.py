from  selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))


    def element_are_visible(self, locator, timeout=5):
        return Wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        self.driver.execute_script('document.querySelector("#app > footer").remove();')
       # self.driver.execute_script('document.getElementById("fixedban").style.display="none"')
        self.driver.execute_script('document.querySelector("#close-fixedban").remove()')