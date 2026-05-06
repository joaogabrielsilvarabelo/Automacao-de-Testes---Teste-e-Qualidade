from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.primeiro_nome_field = (By.ID, "first-name")
        self.sobrenome_field = (By.ID, "last-name")
        self.cep_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def preencher_dados_pessoais(self, nome, sobrenome, cep):
        self.driver.find_element(*self.primeiro_nome_field).send_keys(nome)
        self.driver.find_element(*self.sobrenome_field).send_keys(sobrenome)
        self.driver.find_element(*self.cep_field).send_keys(cep)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def finalizar_compra(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def obter_mensagem_sucesso(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        ).text