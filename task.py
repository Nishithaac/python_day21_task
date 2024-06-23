"""
Using Python Selenium Automation  and the URL https://www.saucedemo.com/ display the
Cookie created before login and after login in the console. After you log in into the dashboard of
the portal kindly do the logout also

verify that the Cookies are being generated during the Login process
"""

# Importing the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Creating a class to handle cookie-related operations
class Cookies:

    # Initializing the class with URL and starting a Chrome WebDriver session
    def __init__(self,url):
        self.url=url
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Method to capture cookies before login
    def cookies_before_login(self):

        # Maximizing the window and navigating to the URL
        self.driver.maximize_window()
        self.driver.get(self.url)

        # Capturing cookies before any action (Initial page load)
        cookies_before_login=self.driver.get_cookies()
        print("Cookies before login: ",cookies_before_login)
        # Returning captured cookies for later use
        return cookies_before_login

    # Method to perform login and capture cookies after login
    def cookies_after_login(self):

        # Entering hardcoded credentials and performing login action
        self.driver.find_element(by=By.ID,value="user-name").send_keys("standard_user")
        self.driver.find_element(by=By.ID,value="password").send_keys("secret_sauce")
        self.driver.find_element(by=By.ID,value="login-button").click()

        # Capturing cookies after successful login
        cookies_after_login=self.driver.get_cookies()
        print("Cookies after login: ",cookies_after_login)
        # Returning captured cookies for later use
        return cookies_after_login


    # Method to verify if new cookies were generated during the login process
    def verify_cookies_generation(self,cookies_before_login,cookies_after_login):

        # Comparing the length of cookies before and after login
        if len(cookies_after_login) > len(cookies_before_login):
            print("Cookies were generated during the process.")
        else:
            print("No new cookies were generated during the login process.")

    # Method to perform logout action
    def logout(self):

        # Opening the menu and clicking on logout
        self.driver.find_element(by=By.ID,value="react-burger-menu-btn").click()
        # Adding a brief delay to ensure the menu operations
        sleep(2)
        self.driver.find_element(by=By.ID,value="logout_sidebar_link").click()
        # Closing the WebDriver session
        self.driver.quit()








# Main entry point of the script
if __name__=="__main__":
    # URL of the Sauce Labs demo website
    url="https://www.saucedemo.com/"
    # Creating an instance of the Cookies Class
    cookies=Cookies(url)
    # Capturing cookies before any action
    cookies_before=cookies.cookies_before_login()
    #Performing login and capturing cookies after successful login
    cookies_after=cookies.cookies_after_login()
    # Verifying if new cookies were generated during the login process
    cookies.verify_cookies_generation(cookies_before,cookies_after)
    # Performing logout to complete the session
    cookies.logout()
