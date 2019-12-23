import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.display_page import DisplayPage
import time



class TestDispaly:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)


    def test_display_huyanmoshi(self):
        self.display_page.click_huyanmoshi()



    def test_display_yejianmoshi(self):
        # 点击显示
        self.display_page.click_night()




    def teardown(self):
        self.driver.quit()