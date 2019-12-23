import os,sys
sys.path.append(os.getcwd())
from page.message_page import MessagePage
from base.base_driver import init_driver
import time

class TestMessage():
    def setup(self):
        self.driver = init_driver()
        self.message_page = MessagePage(self.driver)


    def test_no_disturbing(self):

        #点击显示
        self.message_page.click_no_disturbing()



    def test_led_light(self):
        # 点击显示
        self.message_page.click_led_light()




    def teardown(self):
        self.driver.quit()