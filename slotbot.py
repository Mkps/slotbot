from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type: ignore
from getpass import getpass
import time
from datetime import date

def elem_xpath_text(driver, msg):
     driver.find_element(By.XPATH,"//*[contains(text(), '" + msg + "')]").click()

def matching_days(driver, slot):
    today = date.today().day
    # print(today)
    days = driver.find_elements(By.CLASS_NAME, "fc-day-header")
    for day in days:
        elem = day.get_attribute("outerText")
        str = elem.rpartition("/")
        if int(str[2]) == int(today):
            location = day.location
            x = int(location['x'])
            size = day.size
            width = int(size['width'])
            plus = x + width / 2
            minus = x - width / 2
            loc_slot = slot.location
            x_slot = int(loc_slot['x'])
            if (x_slot >= minus and x_slot <= plus):
                return 1
    return 0

def calendar_refresh(driver):
    driver.refresh()
    time.sleep(1)
    slots = driver.find_elements(By.CLASS_NAME, "fc-time")
    for slot in slots:
        start = slot.get_attribute("data-full") 
        if start:
            value = matching_days(driver, slot)
            if value == 1:
                slot.click()
                time.sleep(5)
                elem_xpath_text(driver, 'OK')
                time.sleep(1)
                return 1
    return 0

def auth_routine(username, password, driver):
    title = driver.title
    assert title == "Sign in to Realm for 42 students"
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.ID, 'kc-login').click()

def exit_routine(username, driver):
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
    driver.implicitly_wait(0.5)
    auth_routine(username, password, driver)
    time.sleep(0.5)
    elem_xpath_text(driver, project)
    title = driver.title
    project_title = "Intra Projects " + project
    assert title == project_title
    time.sleep(0.5)
    elem_xpath_text(driver, 'Subscribe to defense')
    x = 0
    while x < nb_slot:
        x += calendar_refresh(driver)
    time.sleep(1)
    exit_routine(username, driver)

project = input("Enter project name: ")
nb_slot = int(input("How many slot do you need? "))
username = input("Enter your username: ")
password = getpass("Enter your password: ")
bot_routine(username, password, project, nb_slot)
