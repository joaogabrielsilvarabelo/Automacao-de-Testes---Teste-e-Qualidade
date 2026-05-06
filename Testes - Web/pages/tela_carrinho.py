from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.carrinho_icone = (By.CLASS_NAME, "shopping_cart_link")
        self.botao_checkout = (By.ID, "checkout")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def adicionar_produto(self, produto_id):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{produto_id}"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_badge)
        )

    def abrir_carrinho(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.carrinho_icone)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart")
        )

    def ir_para_checkout(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_checkout)
        ).click()
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("checkout-step-one")
        )