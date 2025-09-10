from selenium.webdriver.common.by import By


class ProfileLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
