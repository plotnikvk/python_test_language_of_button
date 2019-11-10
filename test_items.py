import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    expect_text = "Язык не определен!"
    browser.get(link)
    language = browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
    if language == 'es':
        expect_text = "Añadir al carrito"
    elif language == 'fr':
        expect_text = "Ajouter au panier"
    elif language == 'ru':
        expect_text = "Добавить в корзину"
    elif language == 'it':
        expect_text = "Aggiungi al carrello"
    elif language == 'pt':
        expect_text = "Adicionar ao carrinho"
    print(expect_text)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.text == expect_text, f"Текст кнопки не соответствует ожидаемому, Получили: {button.text}"
    time.sleep(30)