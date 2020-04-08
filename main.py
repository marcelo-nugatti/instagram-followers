#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Bot Instagram Followers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import username_instagram, password_instagram
import time


class BotInstagram():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def instagram_url(self):
        time.sleep(3)
        self.driver.get("https://www.instagram.com/")

    def instagram_login(self):
        time.sleep(10)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        username.send_keys(username_instagram)

        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(password_instagram)
        
        time.sleep(3)
        button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        button.click()
        time.sleep(7)

    def instagram_ntf(self):
        ntf = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        ntf.click()

    def instagram_see_all(self):
        see_all = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[3]/div[1]/a')
        see_all.click()
        time.sleep(7)


    def instagram_follow(self):
        follow = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/button')
        follow.click()
        time.sleep(3)
        reload_url = self.driver.get("https://www.instagram.com/explore/people/suggested/")
        time.sleep(3)

    def instagram_loop(self):
        while True:
            self.instagram_follow() 



if __name__ == '__main__':
    bot = BotInstagram()
    bot.instagram_url()
    bot.instagram_login()
    bot.instagram_ntf()
    bot.instagram_see_all()
    bot.instagram_loop()



