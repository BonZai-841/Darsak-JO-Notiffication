from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://darsak.gov.jo/auth/login")
assert "منصة درسك التعليمية" in driver.title

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

# ----------Press Log In-------------
driver.find_element_by_id("loginButton").click()
