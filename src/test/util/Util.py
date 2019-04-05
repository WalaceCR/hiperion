from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.data.config import settings


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

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)

    def finish_browser(self):
        self.driver.delete_all_cookies()
        #self.driver.close()will close only the current chrome window.
        self.driver.quit() #should close all of the open windows, then exit webdriver.


utilidades = Util.get_instance()
