import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_read_data import readYaml
import pytest




class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)


    @pytest.mark.parametrize('content',readYaml("./data/text.yaml")["test001"])
    def test_search001(self,content):
        # 点击显示
        self.search_page.search_input_text(content)
        assert 1


    @pytest.mark.parametrize("content",readYaml("./data/text.yaml")["test002"])
    def test_search002(self,content):
        # 点击显示
        self.search_page.search_input_text(content)
        assert 1


    def teardown(self):
        self.driver.quit()