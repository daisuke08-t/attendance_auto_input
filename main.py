from constants import Constants
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

class Main:
     def main(self):
          dotenv_path = join(dirname(__file__), '.env')
          load_dotenv(dotenv_path)

          driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"))
          # driver.get("https://www.google.com/")

          #マネーフォワードログインページ
          driver.get("https://attendance.moneyforward.com/employee_session/new")
          time.sleep(2)

          #会社ID入力
          input_corporation_id = driver.find_element_by_xpath("//*[@id='employee_session_form_office_account_name']")
          input_corporation_id.send_keys(os.environ.get("CORPORATION_ID"))
          #メールアドレス入力
          input_email_address = driver.find_element_by_xpath("//*[@id='employee_session_form_account_name_or_email']")
          input_email_address.send_keys(os.environ.get("EMAIL_ADDRESS"))
          #パスワード入力
          input_password = driver.find_element_by_xpath("//*[@id='employee_session_form_password']")
          input_password.send_keys(os.environ.get("PASSWORD"))
          #ログイン押下
          click_login = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/div[4]/input")
          click_login.click()

          #日時勤怠押下
          click_attendance = driver.find_element_by_xpath("//*[@id='kt-attendance-header-navigation-item-attendances']/a")
          click_attendance.click()

          # time.sleep(3)
          # #使い方ツアー閉じる
          # for i in driver.find_elements_by_xpath("//*[@id='karte-3711897']/div[2]/div/div/section/div/div/button"):
          #      i.click()

          #txt = driver.find_element_by_class_name("attendance-table-header-month-range-text").text
          # for i in driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/span[1]"):
          #      txt = i.find_element_by_class_name("attendance-table-header-month-range-text").text
          #print(txt)

          #一括編集押下
          click_bulk_editing = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/a[1]')
          click_bulk_editing.click()

          time.sleep(3)

          for i, g in enumerate(driver.find_elements_by_class_name("column-day")):
               if(i == 0):
                    continue

               path_week_day = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[2]/div".format(i)

               for j in driver.find_elements_by_xpath(path_week_day):
                    if(j.text == Constants.WEEKDAY):
                         plus_come_in_cou = 2
                         going_to_work_time = "9:00"
                         leaving_work_time = "18:30"
                         before_rest_in_time = "12:00"
                         before_rest_return_time = "12:45"
                         after_rest_in_time = "17:30"
                         after_rest_return_time = "18:00"
                         #勤務時間帯を選択
                         path_select = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[3]/select".format(i)
                         select = Select(driver.find_element_by_xpath(path_select))
                         select.select_by_value(Constants.WORKING_HOURS[8])
                         #出勤時間を入力
                         psth_2 = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[4]/div/input".format(i)
                         input_going_to_work = driver.find_element_by_xpath(psth_2)
                         input_going_to_work.send_keys(going_to_work_time)
                         #退勤時間を入力
                         path_leaving_work = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[5]/div/input".format(i)
                         input_leaving_work = driver.find_element_by_xpath(path_leaving_work)
                         input_leaving_work.send_keys(leaving_work_time)
                         #指定数分の休憩枠追加
                         if(plus_come_in_cou != None):
                              for plus in range(plus_come_in_cou):
                                   plus = plus + 1
                                   #休憩入りの枠追加
                                   path_plus_come_in = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[6]/div/a[1]".format(i)
                                   click_plus_come_in = driver.find_element_by_xpath(path_plus_come_in)
                                   click_plus_come_in.click()
                                   #休憩戻りの枠追加
                                   path_plus_return = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[7]/div/a[1]".format(i)
                                   click_plus_return = driver.find_element_by_xpath(path_plus_return)
                                   click_plus_return.click()
                         
                                   #休憩入り時間入力
                                   path_before_rest_in = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[6]/div[{}]/input".format(i, plus)
                                   input_before_rest_in = driver.find_element_by_xpath(path_before_rest_in)
                                   input_before_rest_in.send_keys(before_rest_in_time)
                                   #休憩戻り時間入力
                                   path_before_rest_return = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{}]/td[7]/div[{}]/input".format(i, plus)
                                   input_before_rest_return = driver.find_element_by_xpath(path_before_rest_return)
                                   input_before_rest_return.send_keys(before_rest_return_time)

          #保存ボタン押下
          # path_save = "/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/input[2]"
          # for i in driver.find_elements_by_xpath(path_save):
          #      i.submit()

          time.sleep(1)
          driver.quit()