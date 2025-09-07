from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, 'Пароль')
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    RESTORE_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')
