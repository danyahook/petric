from abc import ABC

from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from webdriver_manager.chrome import ChromeDriverManager


class BaseParser:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')
        # self.options.add_argument('--no-sandbox')
        # self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.wait = WebDriverWait(self.driver, 1000)

    def is_site_load(self, element):
        try:
            self.wait.until(EC.presence_of_element_located(element))
        except TimeoutException:
            return False

        return True
