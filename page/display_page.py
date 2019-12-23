import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):#继承BaceAction类，就获得了对象


    display_btn = By.XPATH, "//*[contains(@text,'显示')]"
    huyanmoshi  = By.XPATH, "//*[contains(@content-desc,'护眼模式')]"
    night       = By.XPATH, "//*[contains(@content-desc,'夜间模式')]"





    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.display_btn)




    #点击护眼模式
    def click_huyanmoshi(self):
        self.click(self.huyanmoshi)
        time.sleep(1)

        self.click(self.huyanmoshi)




    def click_night(self):
        self.click(self.night)
        time.sleep(1)
        self.click(self.night)


