import os, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    user = os.environ['COMCAST_USER']
    password = os.environ['COMCAST_PASSWORD']
    # Load login page
    login_page = "https://login.xfinity.com/login"
    driver.get(login_page)
    # Enter creds
    driver.find_element(By.ID, "user").send_keys(user)
    driver.find_element(By.ID, "passwd").send_keys(password)
    # Submit
    driver.find_element(By.ID, "sign_in").click()

def check_status():
    # Load status page
    status_page = "https://www.xfinity.com/support/status/"
    driver.get(status_page)
    # Wait for page load (barbaric)
    time.sleep(10)
    status_banner = driver.switch_to.active_element.text
    # Assert there is no outage
    if "Everything looks good on our end." not in status_banner:
        alert_about_outage()


def alert_about_outage():
    # TODO Add logic here to alert via Email, SMS, Slack, w/e
    print('ahhh there is an outage')


def main():
    login()
    check_status()

# Gloabl driver until refactored out
driver_location = os.path.abspath(os.path.join('drivers', 'linux', 'geckodriver'))
driver = webdriver.Firefox(executable_path=driver_location)

if __name__ == '__main__':
    main()
