from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import allure


class BasePage:
    @allure.title('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открываем заданную страницу по URL с ожиданием ее загрузки')
    def open_page(self, url):
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        try:
            elem = self.wait.until(EC.element_to_be_clickable(locator))
            elem.click()
        except ElementClickInterceptedException:
            # Если клик перехвачен, используем JavaScript
            elem = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", elem)

    @allure.step('Ищем элемент с ожиданием его появления в DOM страницы')
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Ищем элемент c ожиданием его видимости')
    def find_element_with_visibility_wait(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверяем что элемент невидим')
    def wait_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Проверяем что в элементе нет заданного текста')
    def check_no_text_in_element(self, locator, text):
        return self.wait.until_not(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Ожидаем загрузки страницы')
    def wait_for_page_ready(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element_with_visibility_wait(locator)

    @allure.step('Ищем по локатору поле ввода и отправляем в него текст')
    def input_text(self, locator, text):
        self.find_element_with_visibility_wait(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.find_element_with_visibility_wait(locator).text

    @allure.step('Ищем элемент с заданным текстом')
    def find_element_with_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
        element = self.driver.find_element(*locator)
        return element

    @allure.step("Получаем текущий url сайта")
    def get_page_url(self):
        return self.driver.current_url

    @allure.step("Получаем имя браузера")
    def get_browser_name(self):
        return self.driver.capabilities["browserName"].lower()

    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.driver.execute_script(script, source_element, target_element)
