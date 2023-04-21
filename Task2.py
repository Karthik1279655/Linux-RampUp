from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/u/chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.google.com/")
print(driver.title)
search = driver.find_element(By.NAME, 'q')
search.send_keys("Online Python compiler")   #search the online compiler
search.submit()
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3").click() #select the online compiler

driver.find_element(By.XPATH,"//*[@id='editor']").click()
time.sleep(2)

action = ActionChains(driver)
action.key_down(Keys.CONTROL)
action.send_keys("a")
action.key_up(Keys.CONTROL)
action.key_down(Keys.CONTROL)
action.send_keys("x")
action.key_up(Keys.CONTROL)
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.send_keys("s= 'hello world' ")
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.send_keys("key = 'l' ")
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.send_keys("count=s.count(key)")
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.send_keys("print(count)")
action.perform()
run = driver.find_element(By.XPATH,"//*[@id='root']/div[3]/div[4]/div[1]/div[2]/button[3]/span").click()
driver.close()
