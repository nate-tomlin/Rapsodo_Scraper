from selenium import webdriver
from time import sleep
import csv


class Bot:
    def __init__(self, username, password):
        #Accessing Page
        self.driver = webdriver.Chrome()
        self.driver.get("https://cloud.rapsodo.com/2.1/#/auth/login")
        sleep(5)

        #Logging In
        self.driver.find_element_by_xpath('/html/body/app-root/app-guest/app-login/div/div/div/form/div[2]/div[1]/input').send_keys(username)  #Username Field X-Path
        self.driver.find_element_by_xpath('/html/body/app-root/app-guest/app-login/div/div/div/form/div[3]/div[1]/input').send_keys(password)  #Password Field X-Path
        self.driver.find_element_by_xpath('/html/body/app-root/app-guest/app-login/div/div/div/form/div[5]/div[1]/button').click()         #Login Button X-Path
        sleep(10)

    def pitching(self):
        #Selects Pitching Tab
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/app-player-type-selector/ul/li[1]/a').click()
        sleep(5)

        #Expands View To All Players
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/div/div/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/div/div/div/button[5]').click()
        sleep(5)

        #Selects Player /html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/table/tbody/tr[1]/td[2]/div/app-profile-information/div
        player = input("Please Paste in the Players Full XPATH: ")
        name = self.driver.find_element_by_xpath(player).text
        self.driver.find_element_by_xpath(player).click()
        sleep(10)

        #Gets Seesion
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-personal-stats/div[2]/ngb-tabset/ul/li[3]/a').click() #Clicks Sessions
        sleep(10)

        #Gets The Player Session /html/body/app-root/app-auth/main/div/app-personal-stats/div[2]/ngb-tabset/div/div/app-sessions/div[2]/table/tbody/tr
        session = input("Please Paste in the Session Full XPATH: ")
        date = self.driver.find_element_by_xpath(session).text #Gets Session Date
        self.driver.find_element_by_xpath(session).click()
        sleep(2)

        #Gets Column Names Into List
        columns_list = []
        columns = self.driver.find_elements_by_class_name("sortable")
        for column in columns:
            columns_list.append(column.text)
        columns_list.append("PITCH TYPE")
        date_col = 'DATE'
        columns_list.insert(1, date_col)

        #Gets data from session and puts it in a list
        data_list = []
        data = self.driver.find_elements_by_tag_name("tr")
        for i in data:
            row = i.text.split(" ")             #Splits row on space
            row.insert(1, date)
            last_value = row[-1].split("\n")    #Splits last element in row on \n
            row.pop(-1)                         #Reomves last element
            row = row + last_value              #Adds splited last element
            data_list.append(row)               #Adds row to list

        #Removes Empty Strings
        while([""] in data_list): 
            data_list.remove([""]) 

        #Removes List with emptey string and date
        while(["", date] in data_list):
            data_list.remove(["", date])

        #Removes unnessisary header values
        for i in range(len(data_list[0])):
            data_list[0].pop(0)
        for i in range(len(data_list[1])):
            data_list[1].pop(0)

        #Reveses Order of Data List
        data_list.reverse()

        #Creates and Writes to CSV File
        with open(name + '_' + date +'_RapsodoPitchingData.csv', 'w') as fp:
            write = csv.writer(fp, delimiter=',')
            col = columns_list
            data = data_list
            write.writerow(col)     #Writes Header Data
            write.writerows(data)   #Writes Data Rows

        print("")
        print("Data Saved To: " + name + "_" + date + "_RapsodoPitchingData.csv")
        print("")
        self.again()


    def hitting(self):
        #Selects Hitting Tab
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/app-player-type-selector/ul/li[2]/a').click()
        sleep(5)

        #Expands View To All Players
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/div/div/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/div/div/div/button[5]').click()
        sleep(5)

        #Selects Player /html/body/app-root/app-auth/main/div/app-team-management/div[2]/div/ngb-tabset/div/div/app-player/div[2]/app-table/div/table/tbody/tr[1]/td[2]/div/app-profile-information/div
        player = input("Please Paste in the Players Full XPATH: ")
        name = self.driver.find_element_by_xpath(player).text #Gets Players Name
        self.driver.find_element_by_xpath(player).click()
        sleep(10)

        #Gets Seesion
        self.driver.find_element_by_xpath('/html/body/app-root/app-auth/main/div/app-personal-stats/div[2]/ngb-tabset/ul/li[3]/a').click() #Clicks Sessions
        sleep(10)

        #Gets The Player Session /html/body/app-root/app-auth/main/div/app-personal-stats/div[2]/ngb-tabset/div/div/app-sessions/div[2]/table/tbody/tr
        session = input("Please Paste in the Session Full XPATH: ")
        date = self.driver.find_element_by_xpath(session).text #Gets Session Date
        self.driver.find_element_by_xpath(session).click()
        sleep(2)

        #Gets Column Names Into List
        columns_list = []
        columns = self.driver.find_elements_by_class_name("sortable")
        for column in columns:
            columns_list.append(column.text)
        date_col = 'DATE'
        columns_list.insert(1, date_col)

        #Gets data from session and puts it in a list
        data_list = []
        data = self.driver.find_elements_by_tag_name("tr")
        for i in data:
            row = i.text.split(" ")             #Splits row on space
            row.insert(1, date)
            last_value = row[-1].split("\n")    #Splits last element in row on \n
            row.pop(-1)                         #Reomves last element
            row = row + last_value              #Adds splited last element
            data_list.append(row)               #Adds row to list

        #Removes Empty Strings
        while([""] in data_list): 
            data_list.remove([""]) 

        #Removes List with emptey string and date
        while(["", date] in data_list):
            data_list.remove(["", date])

        #Removes unnessisary header values
        for i in range(len(data_list[0])):
            data_list[0].pop(0)
        for i in range(len(data_list[1])):
            data_list[1].pop(0)

        #Reveses Order of Data List
        data_list.reverse()

        #Creates and Writes to CSV File
        with open(name + '_' + date + '_RapsodoHittingData.csv', 'w') as fp:
            write = csv.writer(fp, delimiter=',')
            col = columns_list
            data = data_list
            write.writerow(col)     #Writes Header Data
            write.writerows(data)   #Writes Data Rows
        
        print("")
        print("Data Saved To: " + name + "_" + date + "_RapsodoHittingData.csv")
        print("")
        self.again()


    def again(self):
        again = input("Would you like to get more pitcher data, hitter data, or quit (p/h/q): ")
        if again == "p":
            print("")
            self.driver.back()
            sleep(5)
            print("Getting Pitcher Data.")
            self.pitching()
        elif again == "h":
            print("")
            self.driver.back()
            sleep(5)
            print("Getting Hitter Data.")
            self.hitting()
        elif again == "q":
            self.driver.quit()  #Quits Selenium
            exit()
        else:
            print("Please Enter the correct value (p/h/q).")
            self.again()



def types(username, password):
    #Starts Selenium Bot Based on Pitching or Hitting
    types = input("Pitching or Hitting Data (p/h): ")
    if types == "p":
        print("Getting Pitcher Data.")
        myBot = Bot(username, password)
        myBot.pitching()
    elif types == "h":
        print("Getting Hitter Data.")
        myBot = Bot(username, password)
        myBot.hitting()
    else: 
        print("Please Enter a 'p' or an 'h'.")
        print("Restarting...")
        login()

def login():
    #Login Info
    username = input("Please Enter Your Rapsodo Username/Email: ")
    password = input("Please Enter Your Rapsodo Password: ")
    types(username, password)

def start():
    #Prints Start Scree Graphic
    print("")
    print("")
    print("|------------------------------|")
    print("|  Welcome to Rapsodo Scraper  |")
    print("|------------------------------|")
    print("")
    print("")
    login()

#Starts Script
start()