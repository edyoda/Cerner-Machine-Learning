import time
from selenium import webdriver

from pageObjects.home.login import Auth
from pageObjects.home.dashboard import Sales
from selenium.webdriver import ActionChains

def test_valid_login():
    driver = webdriver.Chrome(executable_path=r"E:\Resourses\automation_testing\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://app.hubspot.com/login")
    driver.maximize_window()
    
    Auth.tb_email(driver).send_keys("")
    Auth.tb_password(driver).send_keys("")
    Auth.btn_password(driver).click()
    time.sleep(10)
    assert "Reports dashboard" == driver.title     
    driver.close()
    
def test_contact_details():
    driver = webdriver.Chrome(executable_path=r"E:\Resourses\automation_testing\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://app.hubspot.com/login")
    driver.maximize_window()
    
    Auth.tb_email(driver).send_keys("")
    Auth.tb_password(driver).send_keys("")
    Auth.btn_password(driver).click()
    time.sleep(10)

    actions = ActionChains(driver)
    actions.move_to_element(Auth.link_contacts(driver)).move_to_element(Auth.link_contacts(driver)).click().perform()
    time.sleep(5)


    driver.close()

    
    
                                    
    
    
    