from selenium import webdriver

from selenium.webdriver import ActionChains
import json
import time

'''
import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
'''


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


def give_attendance():
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

    driver = webdriver.Chrome(
        '/Users/shuhan/research/odoo_auto_attendance/chromedriver')  # Optional argument, if not specified will search path.

    login_to_oddo(driver=driver, odoo_login_link=odoo_login_link, username=username, password=password)

    time.sleep(1)

    driver.get(odoo_attendance_link)

    action = ActionChains(driver)
    startElement = driver.find_element_by_tag_name('body')
    action.move_to_element(startElement)
    action.perform()

    x_i = [20, 30]
    y_i = [20, 30]

    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x, mouse_y);
        action.perform()
        action.click()
        print(mouse_x, mouse_y)
        time.sleep(5)

    driver.save_screenshot('ss.png')
    time.sleep(100)

    # #then key here move to mobile version as that doesn't support javascript
    # browser.get('https://m.facebook.com/'+target_username+'?v=timeline')
    #
    #
    # # find last post (occurance of comment)
    # as_el = browser.find_elements_by_tag_name('a')
    # for a in as_el:
    #     print(a.text)
    #     if 'omment' in a.text.strip():
    #         a.click()
    #         break
    # time.sleep(10)
    #
    # # it will go for 1000 comments
    # i = comment_count
    # while i > 0:
    #     # do actual comment
    #     ins = browser.find_element_by_id('composerInput')
    #
    #     cmnt = getRandomQuote()
    #
    #     ins.send_keys(cmnt)
    #     # submit input
    #
    #     ins = browser.find_elements_by_tag_name('input')
    #     for x in ins:
    #         if 'omment' in x.get_attribute('value'):
    #             x.click()
    #             break
    #
    #     #random waiting
    #     r = random.randrange(2,5)
    #     time.sleep(r)
    #
    #     i = i - 1


if __name__ == "__main__":
    give_attendance()
