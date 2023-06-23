import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pyautogui
import os


class DownloadFile:
    def __init__(self, driver):
        self.driver = driver

    def download_file(self):

        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "/Users/mac/Documents",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        # Open the website and maximize the window
        driver.get("https://demoqa.com/upload-download")
        driver.maximize_window()

        print("Test case started")

        # check for the file upload element to be visible
        click_download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "downloadButton"))).click()

        time.sleep(1)

        #Use pyautogui to handle the download prompt if its shown
        #pyautogui.press('enter')

        #set the time as per file size
        time.sleep(3)

        #verify if the file downloaded successfully and in folder
        download_directory = "/Users/mac/Documents"
        file_name = "sampleFile.jpeg"  # Replace with the actual file name

        file_path = os.path.join(download_directory, file_name)
        if os.path.exists(file_path):
            print("File downloaded successfully!")
        else:
            print("File download failed!")

        print("Test case completed successfully")

uploadfile= DownloadFile(webdriver)
uploadfile.download_file()