from pages.tela_login import LoginPage
from pages.tela_checkout import CheckoutPage
from pages.tela_carrinho import CartPage
from config_web import URL_WEB;

def test_fluxo_e2e_com_sucesso(driver):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    cart_page = CartPage(driver)

    driver.get(URL_WEB)  
    login_page.realizar_login("standard_user", "secret_sauce")
    
    cart_page.adicionar_produto("sauce-labs-backpack")
    cart_page.abrir_carrinho()
    cart_page.ir_para_checkout()

    checkout_page.preencher_dados_pessoais("Jonas", "Tester", "6769420")
    checkout_page.finalizar_compra()

    assert "Thank you for your order" in checkout_page.obter_mensagem_sucesso()