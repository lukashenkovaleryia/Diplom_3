import pytest
from selenium import webdriver
from fakers import generate_user_data
import api
from pages.main import MainPage
from pages.login import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:  # Firefox
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def user():
    user_data = generate_user_data()
    response_info = api.create_user_request(user_data)
    yield user_data
    api.delete_user_request(headers={"Authorization": response_info["accessToken"]})

@pytest.fixture
def auth_user(driver, user):
    main = MainPage(driver)
    main.open()
    main.click_profile_button()
    login = LoginPage(driver)
    login.login_user(user["email"], user["password"])
