from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import autoit
import pyperclip
import schedule
from datetime import date
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

caption ="Test post of Instagram Python Automation \n \n #Algeria"
path = "C:\\Users\\Mohamed\\Desktop\\Insta\\images\\"

print(path)

def job():
    print('entered job')
    print(datetime.now().time())
    filename = next((os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))), "default value here")
    print(filename)
    post(filename)
    os.remove(filename)


def post(jpg_to_post):
    print("enter post()")

    mobile_emulation = { "deviceName": "Nexus 5" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver=webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities = chrome_options.to_capabilities())
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    user_name=driver.find_element_by_xpath("//input[@name='username']")
    user_name.send_keys('Here Put your username or email')
    password=driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys('Here put your Password')
    password.submit()
    #driver.find_element_by_xpath("//*[@class='sqdOP  L3NKy   y3zKF']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[text()='Not Now']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[text()='Cancel']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(2)
    autoit.win_active("Open")
    autoit.control_set_text("Open","Edit1",jpg_to_post)
    autoit.control_send("Open","Edit1","{ENTER}")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//button[@class='_j7nl9']").click()
    except Exception:
        pass
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    time.sleep(2)
    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)
    time.sleep(2)
    #driver.find_element_by_xpath("//*[@class='_qlp0q']").send_keys(Keys.CONTROL, 'v')
    #time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
    time.sleep(5)


    driver.quit()


job()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', hours = 5)
scheduler.start()
