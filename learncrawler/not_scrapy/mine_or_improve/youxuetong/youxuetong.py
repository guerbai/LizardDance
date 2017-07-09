# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global i
i = 50
#第一部分，完成登陆。
driver = webdriver.Chrome()
driver.get("http://www.youxuetong.com/main/tologin.do")
driver.maximize_window()
elem1 = driver.find_element_by_name("loginName")
elem1.clear()
elem1.send_keys("15670937853")
elem2 = driver.find_element_by_name("loginPwd")
elem2.clear()
elem2.send_keys("333315")
elem3 = driver.find_element_by_id("cbxRememberPwd").click()
elem4 = driver.find_element_by_name("btnLogin").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Openloginstatus")))
driver.switch_to_frame("Openloginstatus")
elem5 = driver.find_element_by_xpath("//a[@class='btn_tea']").click()

#循环喽。。
while i < 90 :
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "mainIframe")))
    driver.switch_to_default_content()
    driver.switch_to_frame("mainIframe")
    driver.switch_to_frame("iframe")
    elem6 = driver.find_element_by_xpath("//input[@class='btn5'][2]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aui_loading")))
    #time.sleep(5)aui_content aui_state_full
    driver.switch_to_default_content()
    elem7 = driver.find_element_by_xpath("//iframe")
    s = elem7.get_attribute('name')
    driver.switch_to_frame(s)
    #elem8 = driver.find_element_by_xpath("//tbody/tr[last()]/td[1]/input").click()
    elem8 = driver.find_element_by_xpath("//tbody/tr[3]/td[1]/input").click()
    driver.switch_to_default_content()
    elem9 = driver.find_element_by_xpath("//button[3]").click()
    driver.switch_to_frame("mainIframe")
    driver.switch_to_frame("iframe")
    elem10 = driver.find_element_by_xpath("//textarea[@name='content']")
    elem10.send_keys(u"关注孩子学习，陪伴孩子游戏，给孩子你的时间，让孩子时刻感受到父母的关心和温暖，\
            这是父母给孩子的最珍贵的礼物！远远胜过物质和金钱！你送给孩子幸福的童年、美好的未来，您的现在和将\
            来也会无忧而美满！"+str(i))
    elem11 = driver.find_element_by_class_name('btn_send').click()
    elem12 = driver.find_element_by_class_name('aui_state_highlight').click()
    i += 1
    driver.refresh()
