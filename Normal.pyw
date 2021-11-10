from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import sys
import csv
import ctypes

# ====================================================================================================

srcPath = (__file__)
srcPath = srcPath.replace("\\", "/")
srcPath = srcPath.replace("Normal.pyw", "")

# ====================================================================================================

database = list()

try : 
    f = open(str(srcPath)+"Datavv.csv",'r',encoding='utf-8-sig')
except :
    ctypes.windll.user32.MessageBoxW(0, "데이터를 불러올 수 없습니다.\n폴더 안에 'Data.csv' 파일이 있는지 확인해 주세요.", "자가진단 실패", 0)
    sys.exit()
else :
    readCSV = csv.reader(f)
    for row in readCSV :
        database.append([[row[0]],[row[1]],[row[2]]])
    f.close

# ====================================================================================================

try :
    for x in range (1, len(database)) :

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(str(srcPath) + "driver/chromedriver.exe", options=options)
        driver.implicitly_wait(10)

        driver.get('https://hcs.eduro.go.kr/')

        driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()

# ====================================================================================================

        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button/span').click()
        citySelect = driver.find_element_by_xpath('//*[@id="sidolabel"]')
        citySelector = Select(citySelect)
        citySelector.select_by_value('03')

        levelSelect = driver.find_element_by_xpath('//*[@id="crseScCode"]')
        levelSelector = Select(levelSelect)
        levelSelector.select_by_value('4')

        driver.find_element_by_xpath('//*[@id="orgname"]').send_keys('') # 학교 이름을 입력해주세요
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()

        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click()
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

# ====================================================================================================

        time.sleep(1)
        
        driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(''.join(database[x][0]))
        driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(''.join(database[x][1]))

        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

# ====================================================================================================
        
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="password"]').click()

        time.sleep(0.5)

        key = [driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[4]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[9]/a'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[4]/a'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[1]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[3]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[2]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[2]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[3]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[1]'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[7]/a'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[6]/a'),
                driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[4]')]
        
        keyOriginal = [ "/html/body/div[2]/div[1]/div[8]/a[4]",
                        "/html/body/div[2]/div[1]/div[9]/a",
                        "/html/body/div[2]/div[1]/div[4]/a",
                        "/html/body/div[2]/div[1]/div[5]/a[1]",
                        "/html/body/div[2]/div[1]/div[8]/a[3]",
                        "/html/body/div[2]/div[1]/div[5]/a[2]",
                        "/html/body/div[2]/div[1]/div[8]/a[2]",
                        "/html/body/div[2]/div[1]/div[5]/a[3]",
                        "/html/body/div[2]/div[1]/div[8]/a[1]",
                        "/html/body/div[2]/div[1]/div[7]/a",
                        "/html/body/div[2]/div[1]/div[6]/a",
                        "/html/body/div[2]/div[1]/div[5]/a[4]"]
        
        pwn = [key[0].get_attribute('aria-label'), key[1].get_attribute('aria-label'), key[2].get_attribute('aria-label'),
                key[3].get_attribute('aria-label'), key[4].get_attribute('aria-label'), key[5].get_attribute('aria-label'),
                key[6].get_attribute('aria-label'), key[7].get_attribute('aria-label'), key[8].get_attribute('aria-label'),
                key[9].get_attribute('aria-label'), key[10].get_attribute('aria-label'), key[11].get_attribute('aria-label'),]

        for y in range(0, 12) :
            if pwn[y] == str('빈칸') :
                pwn[y] = '100'

        realPWD = list(str(database[x][2]))

        while "'" in realPWD :    
            realPWD.remove("'")
        realPWD.remove("[")
        realPWD.remove("]")

        for z in range(0, 12) :
            if pwn[z] == realPWD[0] :
                driver.find_element_by_xpath(str(keyOriginal[z])).click()
        time.sleep(0.5)

        for z in range(0, 12) :
            if pwn[z] == realPWD[1] :
                driver.find_element_by_xpath(str(keyOriginal[z])).click()
        time.sleep(0.5)

        for z in range(0, 12) :
            if pwn[z] == realPWD[2] :
                driver.find_element_by_xpath(str(keyOriginal[z])).click()
        time.sleep(0.5)

        for z in range(0, 12) :
            if pwn[z] == realPWD[3] :
                driver.find_element_by_xpath(str(keyOriginal[z])).click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

# ====================================================================================================

        time.sleep(1.5)

        driver.find_element_by_class_name('btn').click()

# ====================================================================================================

        driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
        driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
        driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

        time.sleep(0.5)

        driver.quit()

# ====================================================================================================

except :
    ctypes.windll.user32.MessageBoxW(0, "예상치 못한 오류가 발생했습니다.\n프로그램을 재시작해 주세요.", "자가진단 실패", 0)

# ====================================================================================================

else :
    sys.exit()
