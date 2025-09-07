import allure
from pages.base import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    @allure.step('Кликаем на историю заказов')
    def click_on_history(self):
        self.click_on_element(ProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выходим из профиля')
    def click_on_logout(self):
        self.click_on_element(ProfileLocators.LOGOUT_BUTTON)
        self.wait_invisibility(ProfileLocators.LOGOUT_BUTTON)