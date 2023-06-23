import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Uploadfile:
    def __init__(self, driver):
        self.driver = driver

    def upload_file(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the website and maximize the window
        driver.get("https://demo.guru99.com/test/upload/")
        driver.maximize_window()

        print("Test case started")

        # check for the file upload element to be visible
        file_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uploadfile_0")))

        #pass the file name to the file element
        file_element.send_keys('/Users/mac/Downloads/test-file.jpeg')

        #click on the terms and condition checkbox
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "terms"))).click()

        #click the send file button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "send"))).click()

        time.sleep(1)

        #get the success message
        success_message= driver.find_element(By.CLASS_NAME, "demo").text

        #verify if the file is uploaded successfully
        expected_message= "1 file has been successfully uploaded."
        assert "successfully uploaded." in success_message, f"Success message not displayed expected {expected_message} got {success_message}"

        print("Test case completed successfully")

uploadfile= Uploadfile(webdriver)
uploadfile.upload_file()