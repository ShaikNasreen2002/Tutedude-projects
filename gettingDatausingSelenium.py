from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# Press the Enter key


driver = webdriver.Chrome()

driver.get("http://www.amazon.in")

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("vivo y19")
time.sleep(10) # time in seconds
pyautogui.press('enter') 
list = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']") 
print(len(list)) 
for product in list: 
    print(product.text) 
driver.quit() 