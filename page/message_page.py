import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MessagePage(BaseAction):#继承BaceAction类，就获得了对象


    no_disturbing = By.XPATH, "//*[contains(@content-desc,'免打扰')]"
    message       = By.XPATH, "//*[contains(@text,'通知')]"
    led_light     = By.XPATH, "//*[contains(@text,'LED 指示灯')]"






    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.message)




    #点击护眼模式
    def click_no_disturbing(self):
        self.click(self.no_disturbing)
        time.sleep(1)
        self.click(self.no_disturbing)

    def click_led_light(self):
        self.click(self.led_light)
        time.sleep(1)
        self.click(self.led_light)

