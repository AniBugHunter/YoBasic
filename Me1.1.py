#trying to update Me1 with class and functions

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Herokuapp:
    def __init__(self):
        self.driver = None
        self.driver = webdriver.Chrome()
    def login(self,username, password):
        self.driver.get("https://the-internet.herokuapp.com/")

        link = self.driver.find_element(By.LINK_TEXT, "Form Authentication")
        link.click()

        user_field = self.driver.find_element(By.ID, "username")
        user_field.send_keys(username)

        pass_field = self.driver.find_element(By.ID, "password")
        pass_field.send_keys(password)

        login = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()
        time.sleep(5)
        try:
            self.driver.find_element(By.ID, "flash")
            print("Login Success")
        except:
            print("Login failed!")
            self.driver.quit()
        self.driver.back()
        self.driver.back()
        time.sleep(5)

    def upload_file(self, file_path):
        """Method to upload a file to the Herokuapp website"""

        self.login("tomsmith", "SuperSecretPassword!")
        file_upload_link = self.driver.find_element(By.LINK_TEXT, "File Upload")
        file_upload_link.click()

        # Locate file input and upload file
        self.driver.find_element(By.ID, "file-upload").send_keys(file_path)
        self.driver.find_element(By.ID, "file-submit").click()

        time.sleep(3)  # Wait for confirmation

        # Verify file upload success
        uploaded_file_name = self.driver.find_element(By.ID, "uploaded-files").text
        if uploaded_file_name:
            print(f"File Uploaded Successfully: {uploaded_file_name}")
        else:
            print("File upload failed!")




if __name__ == "__main__":
    validate = Herokuapp()
    #validate.login("tomsmith", "SuperSecretPassword!")
    validate.upload_file("C:\\Users\\anith\\OneDrive\\Desktop\\Automation Input.txt")

