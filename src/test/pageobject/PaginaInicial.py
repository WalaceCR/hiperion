from selenium.webdriver.common.by import By
from src.data.config import settings
from src.test.util.Util import utilidades


class PaginaInicial():

    def __init__(self, driver):
        print("Iniciando a classe Pagina")
        self.txt_pesquisa = driver.find_element(By.NAME, 'q')
        self.btn_pesquisa = driver.find_element(By.NAME, 'btnK')
        self.btn_estou_com_sorte = driver.find_element(By.NAME, 'btnI')
        print("Finalizando a classe Pagina")

    def digitar_pesquisa(self):
        self.txt_pesquisa.send_keys(settings['busca'])

    def clicar_em_pesquisa(self):
        utilidades.aguardar_elemento_clicavel([By.NAME, 'btnK'])
        self.btn_pesquisa.click()
