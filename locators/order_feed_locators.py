from selenium.webdriver.common.by import By


class OrderFeedLocators:
    MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_modal__')]"
    LAST_ORDER = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    ORDER_CONTENT = (By.XPATH, '//p[text()="Cостав"]')
    ORDERS_FOR_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    ORDERS_FOR_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')

    @staticmethod
    def by_order_id(order_id):
        return By.XPATH, f"//p[text()='#0{order_id}']"
