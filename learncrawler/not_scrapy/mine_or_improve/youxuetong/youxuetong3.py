# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains, keys
import time

def login():
    driver = webdriver.Chrome()
    driver.get("http://www.youxuetong.com/main/tologin.do")
    driver.maximize_window()
    elem1 = driver.find_element_by_name("loginName")
    elem1.clear()
    #elem1.send_keys("15670937853")
    elem1.send_keys("18539122639")
    action = action_chains.ActionChains(driver)
    action.move_to_element(driver.find_element_by_id("placeholderPwd")).click()
    #action.send_keys("333315")
    action.send_keys("511236")
    action.perform()
    #elem2 = driver.find_element_by_name("loginPwd")
    #elem2.clear()
    #elem2.send_keys("511236")
    driver.find_element_by_id("cbxRememberPwd").click()
    driver.find_element_by_name("btnLogin").click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "Openloginstatus")))
    time.sleep(1)
    driver.switch_to_frame("Openloginstatus")
    time.sleep(1)
    driver.find_element_by_xpath("//a[@class='btn_tea']").click()
    return driver

def send_msg(driver,i):
    while i < 90 :
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "mainIframe")))
            driver.switch_to_default_content()
            driver.switch_to_frame("mainIframe")
            driver.switch_to_frame("iframe")
            driver.find_element_by_xpath("//input[@class='btn5'][2]").click()
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "aui_loading")))
            #time.sleep(5)aui_content aui_state_full
            driver.switch_to_default_content()
            elem7 = driver.find_element_by_xpath("//iframe")
            s = elem7.get_attribute('name')
            driver.switch_to_frame(s)
            driver.find_element_by_xpath("//tbody/tr[last()-1]/td[4]/input").click()
            #driver.find_element_by_xpath("//tbody/tr[3]/td[1]/input").click()
            driver.switch_to_default_content()
            driver.find_element_by_xpath("//button[3]").click()
            driver.switch_to_frame("mainIframe")
            driver.switch_to_frame("iframe")
            elem10 = driver.find_element_by_xpath("//textarea[@name='content']")
            elem10.send_keys(u"关注孩子学习，陪伴孩子游戏，给孩子你的时间，让孩子时刻感受到父母的关心和温暖，这是\
父母给孩子的最珍贵的礼物！远远胜过物质和金钱！你送给孩子幸福的童年、美好的未来，您的现在和将来也会无忧而美满！"+str(i))
            driver.find_element_by_class_name('btn_send').click()
            driver.find_element_by_class_name('aui_state_highlight').click()
            i += 1
            driver.refresh()
        except Exception:
            print i
            driver.refresh()

if __name__=='__main__':
    global i
    i = 0
    driver = login()
    send_msg(driver,i)
    print 'Ok,done!'