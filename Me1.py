from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
link.click()
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()
time.sleep(5)

try:
    success = driver.find_element(By.ID, "flash")
    print("Login Success")
except Exception:
    print("Login failed!")
    driver.quit()


driver.back()
time.sleep(5)


#driver.quit()
