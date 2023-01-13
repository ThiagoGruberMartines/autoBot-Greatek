#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
import time

navegador = webdriver.Chrome()

navegador.get("http://192.168.1.1/")
time.sleep(2)

navegador.find_element('xpath', '//*[@id="username"]').send_keys("super")
navegador.find_element('xpath', '//*[@id="password"]').send_keys("super123")
navegador.find_element('xpath', '//*[@id="password"]').send_keys(Keys.ENTER) # loga
time.sleep(2)

navegador.find_element('xpath', '//*[@id="checking_buttons"]/a').click() # Pula config rapida
time.sleep(2)


navegador.find_element('xpath', '/html/body/div[3]/div[1]/div/ul/li[2]/a/div[2]').click()
time.sleep(2)
navegador.find_element('xpath', '//*[@id="wanTypeSelect"]').click()
navegador.find_element('xpath', '//*[@id="wanTypeSelect"]/option[4]').click() # altera pra bridge
time.sleep(2)
navegador.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div/form[2]/div[3]/button[1]').click() # salva
time.sleep(7)

navegador.get("http://192.168.1.1/wifi.htm") # Acessa wifi
time.sleep(2)
navegador.find_element('xpath', '//*[@id="htmode_2G"]').click()
navegador.find_element('xpath', '//*[@id="htmode_2G"]/option[1]').click() # largura 20MHz
navegador.find_element('xpath', '//*[@id="htmode_5G"]').click()
navegador.find_element('xpath', '//*[@id="htmode_5G"]/option[3]').click() # largura 80MHz
time.sleep(2)
navegador.find_element('xpath', '//*[@id="channel_2G"]').click()
navegador.find_element('xpath', '//*[@id="channel_2G"]/option[1]').click() # Canal de rádio 2.4 no auto
navegador.find_element('xpath', '//*[@id="channel_5G"]').click()
navegador.find_element('xpath', '//*[@id="channel_5G"]/option[1]').click() # Canal de rádio 5G no auto
time.sleep(2)
navegador.find_element('xpath', '//*[@id="form_id"]/div[7]/span[2]/button[1]/span').click() # Salva
time.sleep(7)

navegador.find_element('xpath', '/html/body/div[3]/div[1]/div/ul/li[4]/a/div[2]').click() # Acessa mesh
time.sleep(2)
navegador.find_element('xpath', '//*[@id="role_disabled"]').click() # Desativa mesh
navegador.find_element('xpath', '//*[@id="MultiAP"]/div[2]/div[8]/span[2]/button[1]/span').click() # Salva
time.sleep(7)

navegador.find_element('xpath', '/html/body/div[3]/div[1]/div/ul/li[6]/a/div[2]').click() # Acessa avançado
navegador.find_element('xpath', '//*[@id="mCSB_1_container"]/ul/li[2]').click() # Config wifi avançado
navegador.find_element('xpath', '//*[@id="ShortGi"]/td[2]/input[2]').click() # Desativa SGI 5G
navegador.find_element('xpath', '/html/body/div[2]/div[2]/div/div/form[2]/div[2]/button[1]').click() # Salva
time.sleep(7)

navegador.find_element('xpath', '/html/body/div[2]/div[2]/div/div/form[2]/div[1]/span[2]/font[1]').click() # Acessa SGI 2.4
navegador.find_element('xpath', '//*[@id="ShortGi"]/td[2]/input[2]').click() # Desativa SGI 2.4
navegador.find_element('xpath', '/html/body/div[2]/div[2]/div/div/form[2]/div[2]/button[1]').click() # Salva
time.sleep(7)

navegador.find_element('xpath', '/html/body/div[2]/div[1]/div/ul/li[5]/a/div[1]/img').click() # Acessa LAN
time.sleep(2)
navegador.find_element('xpath', '//*[@id="ipaddr"]').click() # Clica no ip LAN
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyperclip.copy("192.168.2.5")
pyautogui.hotkey("ctrl", "v")

navegador.find_element('xpath', '//*[@id="gateway"]').click() # Clica no gateway
pyperclip.copy("192.168.2.1")
pyautogui.hotkey("ctrl", "v")

time.sleep(2)
navegador.find_element('xpath', '//*[@id="lan"]/div[4]/div[3]/span[2]/button[2]/span').click() # Salva e aplica

