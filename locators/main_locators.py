from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
    INGREDIENT_ITEM = (By.XPATH, '//p[text()="Соус фирменный Space Sauce"]')

    ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    OVER_WINDOW = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    INGREDIENT_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]')
    ORDER_LIST_READY = (By.CLASS_NAME, 'OrderFeed_orderList__cBvyi')

    BUN_FLUORESCENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    SAUCES = (By.XPATH, '//span[text()="Соусы"]')
    SAUCE_SPICY = (By.XPATH, '//p[text()="Соус Spicy-X"]')

    TOPPINGS = (By.XPATH, '//span[text()="Начинки"]')
    MEAT_METEOR = (By.XPATH, "//img[@alt='Говяжий метеорит (отбивная)']")

    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')

    DEFAULT_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    ORDER_PREPARATION = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class,"title_shadow")]')

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')

    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_CLOSE = (By.XPATH, '//button[contains(@class,"modal__close")]')

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    @staticmethod
    def by_ingredient_name(name):
        return By.XPATH, f"//p[contains(text(), '{name}')]"
