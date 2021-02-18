from selenium import webdriver

from selenium.webdriver import ActionChains
import json
import time
from datetime import datetime


def login_to_oddo(driver, odoo_login_link, username, password):
    # goto login link and give input
    driver.get(odoo_login_link)
    email_elem = driver.find_element_by_id('login')
    email_elem.send_keys(username)

    password_elem = driver.find_element_by_id('password')
    password_elem.send_keys(password)

    time.sleep(1)

    # form submission
    ins = driver.find_elements_by_class_name('oe_login_form')
    for x in ins:
        x.submit()
        break


def main():
    # Opening env.json file
    f = open('env.json', )

    # returns JSON object as a dictionary
    credentials = json.load(f)

    # Closing file
    f.close()

    username = credentials['username']
    password = credentials['password']
    odoo_login_link = credentials['odoo_login_link']
    odoo_attendance_link = credentials['odoo_attendance_link']
    chrome_driver_full_path = credentials['chrome_driver_full_path']

    driver = webdriver.Chrome(chrome_driver_full_path)  # Optional argument, if not specified will search path.

    login_to_oddo(driver=driver, odoo_login_link=odoo_login_link, username=username, password=password)

    time.sleep(5)

    give_attendance(driver=driver, odoo_attendance_link=odoo_attendance_link)


def give_attendance(driver, odoo_attendance_link):
    driver.get(odoo_attendance_link)

    action = ActionChains(driver)
    start_element = driver.find_element_by_tag_name('body')
    action.move_to_element(start_element)
    action.perform()

    x_i = [20, 30]
    y_i = [20, 30]

    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x, mouse_y)
        action.perform()
        action.click()
        print(mouse_x, mouse_y)
        time.sleep(5)

    driver.save_screenshot('screenshots/' + str(datetime.now()) + '.png')
    print('Screen Shot Done')


if __name__ == "__main__":
    main()
