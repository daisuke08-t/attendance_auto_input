import constants

class Check:

    constants = constants.Constants()

    def check_day_of_week(path, driver):
        status = False
        day_of_week = ""

        for i in driver.find_elements_by_xpath(path):
            day_of_week = i.text
            
            print(day_of_week)

        if(day_of_week == constants.WEEKDAY):
            status = True
        return status

