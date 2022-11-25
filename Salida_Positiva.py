from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Archivos de Programa (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://magento.softwaretestingboard.com/')

time.sleep(5) 
sign = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
sign.click()

'''MAIL'''
mail = driver.find_element(By.ID, 'SIGN')
mail.send_keys('matmarano@uade.edu.ar') 
'''CONTRASEÑA'''   
password = driver.find_element(By.ID, 'PASSWORD')
password.send_keys('Daleboca2')
 
clickSign = driver.find_element(By.ID, 'SEND')
clickSign.send_keys(Keys.ENTER)
driver.close()

