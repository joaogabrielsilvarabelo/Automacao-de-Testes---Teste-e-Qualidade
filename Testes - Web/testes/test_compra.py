from pages.tela_login import LoginPage
from pages.tela_checkout import CheckoutPage
from config_web import URL_WEB;

def test_fluxo_e2e_com_sucesso(driver):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    driver.get(URL_WEB)  
    login_page.realizar_login("standard_user", "secret_sauce")
    
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "shopping_cart_container").click()
    driver.find_element("id", "checkout").click()
    
    checkout_page.preencher_dados_pessoais("Jonas", "Tester", "6769420")
    checkout_page.finalizar_compra()

    assert "Thank you for your order" in checkout_page.obter_mensagem_sucesso()