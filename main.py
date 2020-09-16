from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import pandas as pd
from utils import Darsak


# ----------- Global Variables --------------
sign_in = Darsak("2001230470", "2006", "05", "13")
driver = sign_in.driver


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
    sign_in.open_website(url="https://darsak.gov.jo/auth/login")
    sign_in.login_darsak("year", "month", "day", "national_id")
    sign_in.get_parameters()
    full_name = sign_in.full_name
    grade = sign_in.grade
    today_lessons = sign_in.today_lessons
    website_date = sign_in.website_date

    convert_to_csv()
