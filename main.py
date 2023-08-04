from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type: ignore
from selenium.webdriver.support.wait import WebDriverWait #type: ignore
# from selenium.webdriver.support.select import Select 
import time


username = 'username'
password = 'password'
project = 'project'
dropdown_usr = '\n' + username + '\n'
driver = webdriver.Chrome()
url = 'https://profile.intra.42.fr'
# url = 'https://selenium.dev/selenium/web/web-form.html'
# url = 'https://42.fr'
driver.get(url)
time.sleep(2)
title = driver.title
assert title == "Sign in to Realm for 42 students"
driver.implicitly_wait(0.5)
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.ID, 'kc-login').click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[contains(text(), '" + project + "')]").click()
title = driver.title
project_title = "Intra Projects " + project
assert title == project_title
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(), 'Subscribe to defense')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(), '" + dropdown_usr + "')]").click()
time.sleep(1)
x = 0
slots = driver.find_elements(By.CLASS_NAME, "fc-time")
for slot in slots:
    start = slot.get_attribute("data-full") 
    if start:
        print(start)
driver.find_element(By.XPATH, "//*[contains(text(), 'Logout')]").click()
time.sleep(3)
driver.quit()
