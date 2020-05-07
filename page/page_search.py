import allure

import page
from base.base_login import BaseLogin


class PagesSearch(BaseLogin):
    # 点击放大镜按钮
    @allure.step(title="点击搜索")
    def page_click_search(self):
        self.base_click(page.page_search_tool)

    @allure.step(title="输入文字")
    def page_input_search(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(page.page_search_input, text)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.step(title="点击返回")
    def page_click_back(self):
        self.base_click(page.page_search_back)

    def page_search(self, text):
        self.page_click_search()
        self.page_input_search(text)
        self.page_click_back()


