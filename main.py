from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import pandas as pd

# ----------- Global Variables --------------
today_lessons = []
full_name = []
grade = []
website_date = []
# -------------- Sign in credentials --------------
national_id = "2001230470"
year = "2006"
month = "05"
day = "13"
# --------- Use FireFox -----------
driver = webdriver.Firefox()

# ------------- Open darsak.gov.jo and assert ---------------
driver.get("https://darsak.gov.jo/auth/login")
assert "منصة درسك التعليمية" in driver.title


def sign_in():

    time.sleep(1)
    username = driver.find_element_by_id('national_id')
    username.clear()
    username.send_keys(national_id)

    time.sleep(0.5)
    select_year = Select(driver.find_element_by_id("year"))
    select_year.select_by_visible_text(year)

    time.sleep(0.5)
    select_month = Select(driver.find_element_by_id("month"))
    select_month.select_by_visible_text(month)

    time.sleep(0.5)
    select_day = Select(driver.find_element_by_id("day"))
    select_day.select_by_visible_text(day)

    time.sleep(1)

    driver.find_element_by_id("loginButton").click()

# ---------- Find Full Name, Grade Today Lessons and Website Date -----------

# ------------- Daily lessons parameters ---------------


def get_parameters(today_lessons=today_lessons):
    global full_name
    global grade
    global website_date
    try:

        full_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_auth_user_fullname"))

        ).text

        grade = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/h2"))

        ).text

        website_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[3]/div/div[2]/p"))

        ).text

        today_lessons_class_name = driver.find_elements_by_class_name("card-title")
        today_lessons_count = len(today_lessons_class_name)

        for lesson in range(today_lessons_count):
            today_lessons += today_lessons_class_name[lesson].text.split("\n")

    finally:
        print("DONE")


def convert_to_csv():
    csv = pd.DataFrame({
        "حصص اليوم |": today_lessons,
        "اسم الطالب |": full_name,
        "تاريخ اليوم |": website_date,
        "الصف |": grade,

    })
    print(csv)
    csv.to_csv("CSV/Darsak.csv")


if __name__ == "__main__":
    sign_in()
    get_parameters()
    convert_to_csv()
