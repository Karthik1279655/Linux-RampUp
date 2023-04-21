from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="/u/chromedriver")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://kenpoint.sasken.com/hr/intcom/SaskenHolidayList/Holiday%20List%202021.aspx")
time.sleep(20)
driver.find_elements(By.XPATH, "//*[@id='layoutsTable']")
time.sleep(20)

u = driver.find_elements(By.XPATH, "//*[@id='layoutsTable']/tbody/tr/td/div/div/table/tbody/tr[3]/td[2]")
for i in u:
    a = i.text

v = driver.find_elements(By.XPATH, "//*[@id='layoutsTable']/tbody/tr/td/div/div/table/tbody/tr[4]/td[2]")
for i in v:
    b = i.text

w = driver.find_elements(By.XPATH, "//*[@id='layoutsTable']/tbody/tr/td/div/div/table/tbody/tr[5]/td[2]")
for i in w:
    c = i.text

x = driver.find_elements(By.XPATH, "//*[@id='layoutsTable']/tbody/tr/td/div/div/table/tbody/tr[6]/td[2]")
for i in x:
    d = i.text

y = driver.find_elements(By.XPATH,"//*[@id='layoutsTable']/tbody/tr/td/div/div/table/tbody/tr[7]/td[2]")
for i in y:
    e = i.text

month = [a, b, c, d, e]
cnt = 0
for i in month:
    current = month.count(i)
    if current > cnt:
        cnt = current
        holiday = i
print(holiday)
driver.close()


