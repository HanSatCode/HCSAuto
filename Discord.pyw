import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime
import sys
import csv

# ====================================================================================================

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
srcPath = (__file__)
srcPath = srcPath.replace("\\", "/")
srcPath = srcPath.replace("Discord.pyw", "")

# ====================================================================================================

database = list()
discord_Set = list()

try : 
    f = open(str(srcPath)+"Discord_Set.csv",'r',encoding='utf-8-sig')
    readCSV = csv.reader(f)
    for row in readCSV :
        discord_Set.append([row[0],row[1]])
    f.close
except :
    @bot.event
    async def on_ready() :
        channel = bot.get_channel(int(''.join(discord_Set[0][0])))
        Embed = discord.Embed(title="자가진단 실패 - 데이터를 읽을 수 없음", color=0xffcccc)
        await channel.send(embed=Embed)
        sys.exit()
else :
    print("Ready")

try : 
    f = open(str(srcPath)+"Member.csv",'r',encoding='utf-8-sig')
except :
    @bot.event
    async def on_ready() :
        channel = bot.get_channel(int(''.join(discord_Set[0][0])))
        Embed = discord.Embed(title="자가진단 실패 - 데이터를 읽을 수 없음", color=0xffcccc)
        await channel.send(embed=Embed)
        sys.exit()
else :
    readCSV = csv.reader(f)
    for row in readCSV :
        database.append([[row[0]],[row[1]],[row[2]],[row[3]]])
    f.close

# ====================================================================================================

@bot.event
async def on_ready() :
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("자동으로 자가진단"))

    channel = bot.get_channel(int(''.join(discord_Set[0][0])))
    Embed = discord.Embed(title="자가진단 준비 중 - NULL", description="",color=0xb8b8b8)
    msg = await channel.send(embed=Embed)

    time.sleep(0.5)

    try :
        for x in range (1, len(database)) :
            Embed = discord.Embed(title="자가진단 진행 중 - " + str(''.join(database[x][1])),  color=0xffddab)
            await msg.edit(embed=Embed)
            
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

            driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(''.join(database[x][0]))
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()

            time.sleep(0.5)

            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click()
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

# ====================================================================================================

            time.sleep(1)
            
            driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(''.join(database[x][1]))
            driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(''.join(database[x][2]))

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

            realPWD = list(str(database[x][3]))

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
        Embed = discord.Embed(title="자가진단 실패 - '" + str(''.join(database[x][1])) + "' 세션에서 중단됨", color=0xffcccc)
        await msg.edit(embed=Embed)

# ====================================================================================================

    else :
        todayTime = datetime.date.today()
        Embed  = discord.Embed(title="자가진단 완료 - " + str(todayTime.strftime('%y/%m/%d')), color=0xa3ffd4)
        await msg.edit(embed=Embed)
        exit()

# ====================================================================================================

bot.run(''.join(discord_Set[0][1]))