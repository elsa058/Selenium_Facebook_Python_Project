from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Mini_Project_Selenium.Facebook.BaseTest.locators import *
def test_Facebook_ForgetPassword_Functionality_with_Valid_Email():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_Path).click()  # Click Forget Password link
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH,IdentifyEmail_ElementPath)  # Enter Email address
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Valid_Email)
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH,IdentifyYourAccount_ElementPath).text  # Display Identify your account Page
    assert "Identify your account" == IdentifyYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,MyAccount_Button).click()  # Click This is my account button
    sleep(2)
    ResetYourPassword_Page = driver.find_element(By.XPATH,ResetYourPasswordPage_ElementPath).text  # Display Reset Your Password Page
    assert 'Reset Your Password' == ResetYourPassword_Page
    driver.find_element(By.XPATH,SendCodeViaEmailButton_ElementPath).click()  # Select "Send code via email" button
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()  # Click on Continue Button
    sleep(2)
    securityCodePage = driver.find_element(By.XPATH,EnterSecurityCodePage_ElementPath).text  # Display Enter security code page
    assert "Enter security code" == securityCodePage
    sleep(2)
    recovery_code_entry = driver.find_element(By.XPATH,RecoveryCodeEntry_ElementPath)  # Recovery Code Entry
    sleep(2)
    recovery_code_entry.clear()
    recovery_code_entry.send_keys("740515")
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()  # Click on Continue Button
    sleep(2)
    newPassword_Page = driver.find_element(By.XPATH,NewPasswordPage_ElementPath).text  # Display New Password page
    assert "Choose a new password" == newPassword_Page
    newpassword_entry = driver.find_element(By.NAME, "password_new")
    newpassword_entry.send_keys("password1234")
    sleep(2)
    driver.find_element(By.XPATH,NewPassword_ContinueButton).click()  # Click Continue Button
    sleep(2)
    Facebook_Home = driver.current_url  # Display Facebook User Home page
    assert Facebook_Home == "https://www.facebook.com/"
    driver.close()
def test_Facebook_ForgetPassword_Functionality_with_Invalid_Email():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_Path).click()  # Click Forget Password link
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH,IdentifyEmail_ElementPath)  # Enter Email address
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Invalid_Email)  # email address
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    errorMessage = driver.find_element(By.XPATH,NoSearchResults_ErrorMessage).text  # Display Error Message
    assert "No search results" == errorMessage
    driver.close()
def test_Facebook_ForgetPassword_Functionality_with_Null_Email():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword_Path).click()  # Click Forget Password link
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page.
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH,PleaseFillInAtLeastOneField_ErrorMessage).text  # Display Error Message
    assert "Please fill in at least one field" == IdentifyYourAccount_Page
    driver.close()