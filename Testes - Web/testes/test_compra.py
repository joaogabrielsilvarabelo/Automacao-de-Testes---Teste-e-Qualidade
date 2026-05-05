import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from testes.pages.tela_login import LoginPage
from config_web import URL_WEB;

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) 
    yield driver
    driver.quit()

def test_fluxo_compra_completo(driver):
    driver.get(URL_WEB)
    
    login = LoginPage(driver)
    login.realizar_login("standard_user", "secret_sauce")
    
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "shopping_cart_container").click()
    
    driver.find_element("id", "checkout").click()
    driver.find_element("id", "first-name").send_keys("Jose")
    driver.find_element("id", "last-name").send_keys("QA")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "finish").click()
    
    texto_sucesso = driver.find_element("class name", "complete-header").text
    assert "Thank you for your order" in texto_sucesso