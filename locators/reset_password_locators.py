from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SAVE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')