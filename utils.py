from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import pandas as pd


class Darsak:
    def __init__(self, national_num, year, month, day):

        self.year = year
        self.month = month
        self.day = day
        self.national_num = str(national_num)
        self.driver = webdriver.Firefox()
        self.today_lessons = []
        self.archived_lessons = []
        self.full_name = ""
        self.grade = ""
        self.website_date = ""
        self.full_name = ""

    def open_website(self, url):
        self.driver.get(str(url))

    def close_website(self):
        self.driver.quit()
        print("DONE")

    def login_darsak(self, year_id, month_id, day_id, national_id):
        time.sleep(1)
        self.selector(year_id=year_id, month_id=month_id, day_id=day_id, national_id=national_id)
        self.driver.find_element_by_id("loginButton").click()

    def selector(self, year_id, month_id, day_id, national_id):
        username_id = self.driver.find_element_by_id('national_id')
        username_id.clear()
        username_id.send_keys(self.national_num)

        time.sleep(0.5)
        select_year = Select(self.driver.find_element_by_id(year_id))
        select_year.select_by_visible_text(self.year)

        time.sleep(0.5)
        select_month = Select(self.driver.find_element_by_id(month_id))
        select_month.select_by_visible_text(self.month)

        time.sleep(0.5)
        select_day = Select(self.driver.find_element_by_id(day_id))
        select_day.select_by_visible_text(self.day)

    def get_name_grade_website_date(self):
        # Get the full name , grade, website date, today's lessons

        self.full_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_auth_user_fullname"))

        ).text

        self.grade = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/h2"))

        ).text

        self.website_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[3]/div/div[2]/p"))

        ).text

        today_lessons_class_name = self.driver.find_elements_by_class_name("card-title")
        today_lessons_count = len(today_lessons_class_name)

        for lesson in range(today_lessons_count):
            self.today_lessons += today_lessons_class_name[lesson].text.split("\n")
