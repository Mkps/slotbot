from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

username = 'toto'
service = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
url = 'https://profile.intra.42.fr'
# url = 'https://selenium.dev'
driver = webdriver.Chrome(service = service, options=options)
driver.get(url)
time.sleep(1)
sign_in = driver.find_element(By.ID, 'kc-login')
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys(username)
pwd_field = driver.find_element(By.NAME, 'password')
pwd_field.send_keys('pwd0123')
sign_in.click()
# button.click()
# logout = driver.find_element(By.ID, 'Logout')
# logout.click()
dropdown = driver.find_element(By.ID, 'dropdown')
dropdown.click()
# history = driver.find_element(By.LINK_TEXT, "Logout")
# history.click()
time.sleep(3)