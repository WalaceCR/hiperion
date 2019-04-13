from selenium.webdriver.common.by import By
from src.data.config import settings
from src.test.util.Util import utilidades


class PaginaResultados():

    def __init__(self, driver):
        self.resultados = driver.find_element(By.XPATH, "//*[1][@class='g'][1]/div[1]/div[1]/div[1]/a[1]")
        pass

    def clicando_no_item(self):
        self.resultados.click()
