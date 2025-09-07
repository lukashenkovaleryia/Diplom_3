import allure
from pages.main import MainPage
from pages.profile import ProfilePage

@allure.suite("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Входим в окно своего профиля по клику на «Личный кабинет»")
    def test_go_to_profile(self, driver, auth_user):
        main = MainPage(driver)
        main.open()
        main.click_profile_button()
        assert main.get_page_url().endswith('account/profile')

    @allure.title("Переходим в историю заказов по клику на «История заказов»")
    def test_go_the_order_history(self, driver, auth_user):
        main = MainPage(driver)
        main.open()
        main.click_profile_button()

        profile = ProfilePage(driver)
        profile.click_on_history()
        assert profile.get_page_url().endswith('order-history')

    @allure.title("Выходим из профиля по клику на «Выход»")
    def test_logout(self, driver, auth_user):
        main = MainPage(driver)
        main.open()
        main.click_profile_button()

        profile = ProfilePage(driver)
        profile.click_on_logout()
        assert profile.get_page_url().endswith('login')
