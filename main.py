from check import Check
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"))
driver.get("https://www.google.com/")
time.sleep(2)

#マネーフォワードログインページ
driver.get("https://attendance.moneyforward.com/employee_session/new")

time.sleep(3)
#会社ID入力
for i in driver.find_elements_by_xpath("//*[@id='employee_session_form_office_account_name']"):
     i.send_keys(os.environ.get("CORPORATION_ID"))
#メールアドレス入力
for i in driver.find_elements_by_xpath("//*[@id='employee_session_form_account_name_or_email']"):
     i.send_keys(os.environ.get("EMAIL_ADDRESS"))
#パスワード入力
for i in driver.find_elements_by_xpath("//*[@id='employee_session_form_password']"):
     i.send_keys(os.environ.get("PASSWORD"))
#ログイン押下
for i in driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/form/div[4]/input"):
     i.click()

#日時勤怠押下
for i in driver.find_elements_by_xpath("//*[@id='kt-attendance-header-navigation-item-attendances']/a"):
     i.click()

# time.sleep(3)
# #使い方ツアー閉じる
# for i in driver.find_elements_by_xpath("//*[@id='karte-3711897']/div[2]/div/div/section/div/div/button"):
#      i.click()

#txt = driver.find_element_by_class_name("attendance-table-header-month-range-text").text
# for i in driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/span[1]"):
#      txt = i.find_element_by_class_name("attendance-table-header-month-range-text").text
#print(txt)

for i in driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/a[1]'):
     i.click()

time.sleep(3)

# for i, g in enumerate(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody")):
#      print(i)

check = Check()
cou = 0
for i, g in enumerate(driver.find_elements_by_class_name("column-day")):
     if(i == 0):
          continue
     path = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[2]/div".format(i)
     status = check.check_day_of_week(path, driver)

     if(status):
          cou = cou + 1

print(cou)


#/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[1]
#/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[1]/td[1]
# /html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[2]/td[3]
# /html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[3]/td[3]


# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
time.sleep(2)
driver.quit()