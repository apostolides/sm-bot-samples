from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://www.instagram.com/accounts/login/?source=auth_switcher")

time.sleep(1)

name_field = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
name_field.send_keys("") # USERNAME

pass_field = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
pass_field.send_keys("") # PASSWORD

name_field.send_keys(Keys.RETURN)
pass_field.send_keys(Keys.RETURN)

time.sleep(2)



driver.get("https://www.instagram.com/instagram/")


time.sleep(3);

follow_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/button")
follow_button.click()

time.sleep(4);

driver.close()
