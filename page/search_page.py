import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):#继承BaceAction类，就获得了对象



    search_btn   = By.XPATH, "//*[contains(@content-desc,'搜索')]"
    search_input = By.XPATH, "//*[contains(@text,'搜索')]"





    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.search_btn)




    #点击护眼模式
    def search_input_text(self, text):
        self.input(self.search_input,text)




