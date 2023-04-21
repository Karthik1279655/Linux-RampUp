import operator

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class marbles:
    def __init__(self,employe_name,earned_marbles_no,given_marbles_no):
        self.employe_name = employe_name
        self.earned_marbles_no = earned_marbles_no
        self.given_marbles_no = given_marbles_no

marbless_dict ={}

driver = webdriver.Chrome(executable_path="/home/ee212837/PycharmProjects/chromedriver")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://jam.sasken.com/home")
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='home_nav_tabs_container']/div/div/ul/div/ul/li[4]/a/span[1]/span").click()
time.sleep(10)
driver.find_element(By.XPATH, " //a[@title='Virtual Marbles']").click() #clicks the virtual marble
print(driver.current_window_handle)
handles = driver.window_handles        #returns d list of open browser winodows
for handle in handles:
    driver.switch_to.window(handle)
    #print(driver.title)
    # if driver.title == "Sign-in Sasken": # this method closes the particular window by getting the title of the window
    #     driver.close()
driver.find_element(By.XPATH,"//a[@href='Query.aspx']").click() #selects Query option
driver.find_element(By.ID,"ContentPlaceHolder1_rdbtnSearch_1").click()   # selects the required radio button

#search = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$ctl06$txtsearchEmplID')
#search.send_keys("211723")
#search.submit()
#driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$ctl06$txtsearchEmplID").send_keys("2117")


no_emp = int(input("no of emp_id:"))
for i in range(0, no_emp):
    Emp_id = input("emp_id:")
    Id1 = driver.find_element(By.CSS_SELECTOR," #ContentPlaceHolder1_txtsearchEmplID  ").send_keys(Emp_id)
    Id2 = driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolder1_txtsearchEmplID ").send_keys(Keys.ENTER)

    employe_name = driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_Label4']").text
    print(employe_name)

    marbles_earned = driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_lblDearEarned']").text
    earned_marbles_no = int(marbles_earned)
    print("marbles_earned:",earned_marbles_no)

    marbles_given = driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_lblDearGiven']").text
    given_marbles_no = int(marbles_given)
    print("marbles_given: ",given_marbles_no)

    marbless_dict[Emp_id] = marbles(employe_name, given_marbles_no, earned_marbles_no)
    clr = driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolder1_txtsearchEmplID").clear()


cnt1 = 0
print("Top given marbles:")
for marbles in (sorted(marbless_dict.values(), key=operator.attrgetter('given_marbles_no'), reverse=True)):
    if (cnt1 == 3):
        break
    cnt1 += 1
    print(marbles.employe_name)
    print(marbles.given_marbles_no)

cnt2 = 0
print("Top earned marbles:")
for marbles in (sorted(marbless_dict.values(), key=operator.attrgetter('earned_marbles_no'), reverse=True)):
    if (cnt2 == 3):
        break
    cnt2 += 1
    print(marbles.employe_name)
    print(marbles.earned_marbles_no)






