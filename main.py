from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type: ignore
from getpass import getpass
# from selenium.webdriver.support.select import Select 
import time
def elem_xpath_text(driver, msg):
     driver.find_element(By.XPATH,"//*[contains(text(), '" + msg + "')]").click()

def calendar_refresh(driver):
    driver.refresh()
    time.sleep(2)
    slots = driver.find_elements(By.CLASS_NAME, "fc-time")
    for slot in slots:
        start = slot.get_attribute("data-full") 
        if start:
            print(start)
            slot.click()
            time.sleep(1)
            elem_xpath_text(driver, 'Cancel')
            time.sleep(1)
            break

def exit_routine(driver):
    dd_msg = '\n' + username + '\n'
    elem_xpath_text(driver, dd_msg)
    time.sleep(1)
    elem_xpath_text(driver, 'Logout')
    time.sleep(1)
    driver.quit()

def bot_routine(username, password, project, nb_slot):
    driver = webdriver.Chrome()
    url = 'https://profile.intra.42.fr'
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
    d_msg = 'Subscribe to defense'
    elem_xpath_text(driver, d_msg)
    x = 0
    while x < nb_slot:
        calendar_refresh(driver)
        x += 1
    time.sleep(1)
    exit_routine(driver)

project = input("Enter project name: ")
nb_slot = input("How many slot do you need?")
username = input("Enter your username: ")
password = getpass("Enter your password: ")
bot_routine(username, password, project, nb_slot)
