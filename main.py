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

        return download, upload



    def tweet_at_provider(self, down, up):

        self.driver.get("https://twitter.com/?lang=en")
        x_path = '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a'

        time.sleep(25)

        login = self.driver.find_element(By.XPATH, x_path)
        login.click()

        time.sleep(3)

        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)

        time.sleep(25)

        password_ = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_.send_keys(TWITTER_PASSWORD)
        password_.send_keys(Keys.ENTER)

        time.sleep(30)

        tweet = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']/div/div/div/span")
        tweet.send_keys(f"Download: {down}\n Upload: {up}")

        btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        btn.click()

        time.sleep(25)






isn = InternetSpeed(150,50)


down, up = isn.get_internet_speed()
isn.tweet_at_provider(down, up)