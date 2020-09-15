from selenium import webdriver

# --------- Use FireFox -----------
driver = webdriver.Firefox()

# ------------- Open darsak.gov.jo and assert ---------------
driver.get("https://darsak.gov.jo/auth/login")
assert "منصة درسك التعليمية" in driver.title

# ------------- Username (National ID) ---------------
username = driver.find_element_by_id('national_id')
username.clear()
username.send_keys("2001230470")

# ------------ Date of birth --------------
year_of_birth = driver.find_element_by_id("year")
year_of_birth.clear
year_of_birth.send_keys("222222222222222")

month_of_birth = driver.find_element_by_id("month")
month_of_birth.clear
month_of_birth.send_keys("00000")

day_of_birth = driver.find_element_by_id("day")
day_of_birth.clear
day_of_birth.send_keys("13")

# ---------- Log In -------------
driver.implicitly_wait(5)
driver.find_element_by_id("loginButton").click()

