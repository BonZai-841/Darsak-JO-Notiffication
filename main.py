from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import pandas as pd
from utils import Darsak
import os
from send_email import SendEmail


# ----------- Global Variables --------------


email = os.environ.get("BK_EMAIL")
password = os.environ.get("BK_EMAIL_PASS")
reciever = os.environ.get("BK_EMAIL2")

# ------------------------------------------------|
username = os.environ.get("BK_NATIONAL_ID")     # | Darsak credentials
year_of_birth = os.environ.get("BK_YEAR")       # |
month_of_birth = os.environ.get("BK_MONTH")     # |
day_of_birth = os.environ.get("BK_DAY")         # |
sign_in = Darsak(username, year_of_birth,
                 month_of_birth, day_of_birth)
driver = sign_in.driver
# ------------------------------------------------|


archived_lessons = []
full_name = sign_in.full_name
grade = sign_in.grade
today_lessons = sign_in.today_lessons
website_date = sign_in.website_date

# ------------------- Run script -------------------


def convert_to_csv():
    csv = pd.DataFrame({
        # "حصص اليوم |": today_lessons,
        "اسم الطالب |": full_name,
        "تاريخ اليوم |": website_date,
        "الصف |": grade,
        "الحصص الماضية": archived_lessons,

    })
    print(csv)
    csv.to_csv("CSV/Darsak.csv")


def get_archived_lessons():
    global archived_lessons

    sign_in.open_website("https://darsak.gov.jo/students/lessons/archived")

    today_lessons_class_name = driver.find_elements_by_class_name("card-title")
    today_lessons_count = len(today_lessons_class_name)

    for lesson in range(today_lessons_count):
        archived_lessons += today_lessons_class_name[lesson].text.split("\n")
    return archived_lessons


if __name__ == "__main__":
 
    sign_in.open_website(url="https://darsak.gov.jo/auth/login")
    sign_in.login_darsak("year", "month", "day", "national_id")

    sign_in.get_name_grade_website_date()

    full_name = sign_in.full_name
    grade = sign_in.grade
    today_lessons = sign_in.today_lessons
    website_date = sign_in.website_date

    driver.implicitly_wait(10)
    archived_lessons = get_archived_lessons()

    driver.implicitly_wait(10)

    message = "Subject: This test has been done through main.py\n\nhello how are you doing "

    sendemail = SendEmail(email, password, reciever, message)
    sendemail.send_email(sendemail.email, sendemail.password, sendemail.message, sendemail.reciever)

    convert_to_csv()
    driver.close()


