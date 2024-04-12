import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Insta:

    def __init__(self,url):
        self.url=url
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)

    def login(self):
        print("Login success")
        time.sleep(9)

    def following(self):
        ul=self.driver.find_element(By.TAG_NAME,'ul')
        items=ul.find_elements(By.TAG_NAME,'li')
        for li in items:
            print(li.text)

if __name__ =="__main__":
    IL=Insta("https://www.instagram.com/guviofficial/")
    IL.start()
    IL.login()
    IL.following()






