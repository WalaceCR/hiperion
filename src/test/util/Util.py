from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.data.config import settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Util():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Util()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox(GeckoDriverManager().install())
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager(settings['versao_do_driver']).install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager(settings['versao_do_driver']).install())

    def get_driver(self):
        return self.driver

    def start_browser(self):
        self.driver.maximize_window()

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self):
        self.driver.get(settings['url'])

    def finish_browser(self):
        self.driver.delete_all_cookies()
        #self.driver.close()will close only the current chrome window.
        self.driver.quit() #should close all of the open windows, then exit webdriver.

    def aguardar_elemento_clicavel(self, identificacao):
        WebDriverWait(self.get_driver(), 20).until(
        EC.element_to_be_clickable((identificacao)))

    def aguardar_elemento_visivel(self, identificacao):
        WebDriverWait(self.get_driver(), 20).until(
        EC.presence_of_element_located((identificacao)))


utilidades = Util.get_instance()
