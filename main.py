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
driver = webdriver.Chrome(chromedriver_path)