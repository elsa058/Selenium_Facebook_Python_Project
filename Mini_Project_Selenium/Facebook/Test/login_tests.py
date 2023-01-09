from selenium import webdriver
from selenium.webdriver.common.by import By
from Mini_Project_Selenium.Facebook.BaseTest.locators import *
from time import sleep
def test_Facebook_Login_Functionality_with_Valid_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
    sleep(2)
    email.clear()
    email.send_keys("Elsa des")
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_path)
    sleep(2)
    password.clear()
    password.send_keys("Login_Valid_Password")
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(5)
    Facebook_Home = driver.current_url
    assert Facebook_Home == "https://www.facebook.com/"
    driver.close()
def test_Facebook_Login_Functionality_with_Invalid_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
    sleep(2)
    email.clear()
    email.send_keys("Login_Invalid_Email")
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_path)
    sleep(2)
    password.clear()
    password.send_keys(Login_Invalid_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button.
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_Invalid_EmailAndPassword_ErrorMessage).text
    assert 'Invalid username or password' == Error_message
    sleep(5)
    driver.close()
def test_Facebook_Login_Functionality_with_Valid_Email_and_Invalid_Password():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
    sleep(2)
    email.clear()
    email.send_keys("Login_Valid_Email")
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_path)
    sleep(2)
    password.clear()
    password.send_keys(Login_Invalid_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_ValidEmail_And_InvalidPassword_ErrorMessage).text
    assert 'Invalid username or password' == Error_message
    sleep(5)
    driver.close()

def test_Facebook_Login_Functionality_with_Invalid_Email_and_Valid_Password():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
    sleep(2)
    email.clear()
    email.send_keys("Login_Invalid_Email")
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password_path)
    sleep(2)
    password.clear()
    password.send_keys("Login_Valid_Password")
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_InvalidEmail_And_ValidPassword_ErrorMessage).text
    assert 'Invalid username or password' == Error_message
    sleep(5)
    driver.close()
def test_Facebook_Login_Functionality_with_Blank_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()  # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_Blank_EmailAndPassword_ErrorMessage).text
    assert "Find your account and log in." == Error_message
    sleep(5)
    driver.close()