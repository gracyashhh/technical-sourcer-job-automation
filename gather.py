from time import sleep
from selenium import webdriver
from config import USERNAME_LINKEDIN as USERNAME,PASSWORD_LINKEDIN as PASSWORD
Chromedriver=r"C:\Users\dell\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(Chromedriver)
# Backup URL
URL="https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
driver.get(URL)
driver.maximize_window()
username='//*[@id="username"]'
driver.find_element_by_xpath(username).send_keys(USERNAME)
pswd='//*[@id="password"]'
driver.find_element_by_xpath(pswd).send_keys(PASSWORD+"\n")
# Query in the url
goto="https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103644278%22%5D&companySize=%5B%22C%22%2C%22D%22%2C%22E%22%5D&origin=FACETED_SEARCH&sid=0c3"
driver.get(goto)

company_link=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span/span/a').click()
sleep(4)
company_name=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/h1/span').text
print(company_name)
driver.get(goto)

company_link2=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li[2]/div/div/div[2]/div[1]/div[1]/div/span/span/a').click()
print(company_name)
sleep(4)

company_name=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/h1/span').text
print(company_name)

about = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a')
about.click()
sleep(3)
count_of_employees = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[3]').text
print(count_of_employees)
location = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[1]').text
print(location)
website = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[3]/div[1]/div[1]/a').get_attribute('href')
print(website)
specialities = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[8]').text
print(specialities)