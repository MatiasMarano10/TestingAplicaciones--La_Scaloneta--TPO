import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def TestPositivo():
    PATH= "C:\Archivos de Programa (x86)\chromedriver.exe"
    driver=webdriver.Chrome(PATH)

    driver.get('https://magento.softwaretestingboard.com/')

    time.sleep(5)
    sign=driver.find_element(By.LINK_TEXT,'Sign In')
    sign.click()

    time.sleep(3)
    mail=driver.find_element(By.ID,'email')
    mail.send_keys('matmarano@uade.edu.ar')

    time.sleep(1)
    password=driver.find_element(By.ID,'pass')
    password.send_keys('Daleboca2')
    password.send_keys(Keys.ENTER)
    time.sleep(5)

def __main__():
    TestPositivo()

if __name__ == '__main__':
    __main__()
