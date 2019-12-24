from selenium  import  webdriver
from selenium.webdriver.support.select import Select
import time
import random
driver = webdriver.Chrome()
driver.get("http://10.19.160.155:8877/%E5%BF%AB%E9%80%92%E6%8A%8A%E6%9E%AA%E6%89%AB%E6%8F%8F.html")
driver.maximize_window()

listId = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/span/table/tbody/tr[7]/td[3]/input")
isNormal = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/span/table/tbody/tr[26]/td[3]/input")

Select(driver.find_element_by_tag_name("select")).select_by_visible_text("快件签收")

#网点编码
wdid = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/span/table/tbody/tr[6]/td[7]/input")
appendData = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/span/table/tbody/tr[1]/td/button[1]")
submitBtn = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/span/table/tbody/tr[1]/td/button[2]")


yyw = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/span/table/tbody/tr[16]/td[7]/input")
yyw2 = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/span/table/tbody/tr[14]/td[7]/input")
#创建扫描记录
listNumber = 2019121888001
# wds = [317024,610008,201713]
while True:
    wdid.clear()
    # wdid.send_keys(wds[random.randint(0,2)])
    wdid.send_keys("201701")
    listId.clear()
    listId.send_keys(listNumber)
    isNormal.clear()
    isNormal.send_keys("01")
    yyw.clear()
    yyw.send_keys("1001")
    yyw2.clear()
    yyw2.send_keys("1001")
    appendData.click()

    listNumber += 1
    if listNumber == 2019121888050555:
        submitBtn.click()
        time.sleep(3)
        driver.close()
        break




