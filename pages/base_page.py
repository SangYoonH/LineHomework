#  filename: pages/base_page.py
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _click2(self, locator):
        self._find(locator).send_keys(Keys.ENTER)

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _type_and_click2(self, locator, input_text):
        self._click(locator)
        self._find(locator).send_keys(input_text).send_keys(Keys.ENTER)

    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _get_title(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.title_contains(
                    (locator['value'])))
        except TimeoutException:
            return False
        return True

    def _cannot_get_title(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.title_contains(
                    (locator['value'])))
        except TimeoutException:
            return True
        return False

    def _click_inarow(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
            self._find(locator).send_keys(Keys.ENTER)

        except TimeoutException:
            return False
        return True

    def _select(self, locator, input_select):
        select = Select(self._find(locator))
        select.select_by_visible_text(input_select)

    def _click_inarow2(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
            self._find(locator).click()

        except TimeoutException:
            return False
        return True

    def _is_not_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])))

            except TimeoutException:
                return True
            return False
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return True

    def _reset(self, locator):
        self._find(locator).clear()








