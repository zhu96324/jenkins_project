import pytest
import allure
from base.base_driver import init_drvier
from page.page_search import PagesSearch


class TestSearch:

    def setup(self):
        self.driver = init_drvier()
        self.page_search = PagesSearch(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.feature("搜索框输入内容")
    @allure.severity("BLOCKER")
    @pytest.mark.parametrize("text", ["xiaoming", "hello"])
    def test_search(self, text):
        self.page_search.page_search(text)