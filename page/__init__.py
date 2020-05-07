"""以下为设置搜索框元素定位参数配置信息"""
from selenium.webdriver.common.by import By

page_search_tool = By.XPATH, "//*[@content-desc='搜索']"

page_search_input = By.XPATH, "//*[@text='搜索…']"

page_search_back = By.XPATH, "//*[@content-desc='收起']"
