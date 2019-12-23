from selenium.webdriver.support.wait import WebDriverWait
import yaml
class BaseAction:

    def __init__(self, driver):
        self.driver = driver



    def find_element(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    def find_elements(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(loc[0], loc[1]))

    '''
        自己重写了系统的find_element方法，调用的时候就不要加self.driver.find...直接self.find
    '''

    #定义点击函数，传入元素
    def click(self, loc):
        self.find_element(loc).click()

    #定义输入，传入元素，输入文本
    def input(self, loc, text):
        self.find_element(loc).send_keys(text)

    def readYaml(self,filepath):
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
            print(type(data))  # 打印data类型
            print(data)  # 打印data返回值



