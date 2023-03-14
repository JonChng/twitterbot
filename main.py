from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv
import os
import time

dotenv.load_dotenv()

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']

up = 50
down = 150

class InternetSpeed:

    def __init__(self, up, down):
        self.driver = webdriver.Chrome(chromedriver_path)
        self.link = "https://www.speedtest.net/"
        self.download = down
        self.upload = up

    def get_internet_speed(self):
        self.driver.get(self.link)
        time.sleep(5)

        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()

        time.sleep(60)

        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download: {download}\nUpload: {upload}")



    def tweet_at_provider(self):
        pass

isn = InternetSpeed(150,50)


isn.get_internet_speed()