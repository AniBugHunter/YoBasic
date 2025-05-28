from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HerokuAppAutomation:
    def __init__(self):
        """Initialize WebDriver"""
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        """Method to login into the Herokuapp website"""
        self.driver.get("https://the-internet.herokuapp.com/")

        # Click 'Form Authentication'
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()

        # Enter login credentials
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

        # Click login button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)  # Wait for page load

        # Verify login success
        try:
            success_message = self.driver.find_element(By.ID, "flash").text
            print(f"Login Success: {success_message}")
        except Exception:
            print("Login failed!")

    def upload_file(self, file_path):
        """Method to upload a file to the Herokuapp website"""
        self.driver.get("https://the-internet.herokuapp.com/upload")

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

    def close_browser(self):
        """Method to close the browser"""
        self.driver.quit()


# Execute the script
if __name__ == "__main__":
    automation = HerokuAppAutomation()
    automation.login("tomsmith", "SuperSecretPassword!")  # Replace with valid credentials
    automation.upload_file("C:\\Users\\anith\\OneDrive\\Desktop\\Automation Input.txt")  # Replace with the actual file path
    automation.close_browser()