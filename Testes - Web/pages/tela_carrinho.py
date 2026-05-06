from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.carrinho_icone = (By.ID, "shopping_cart_container")
        self.botao_checkout = (By.ID, "checkout")

    def adicionar_produto(self, produto_id):
        self.driver.find_element(By.ID, f"add-to-cart-{produto_id}").click()

    def abrir_carrinho(self):
        self.driver.find_element(*self.carrinho_icone).click()

    def ir_para_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_checkout)
        ).click()