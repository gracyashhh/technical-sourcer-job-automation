from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyautogui as pa
from config import USERNAME_ASANA as USERNAME,PASSWORD_ASANA as PASSWORD


Chromedriver=r"C:\Users\dell\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"

CHECK_FOR=['TED Conferences','Forbes']

driver=webdriver.Chrome(Chromedriver)
driver.maximize_window()


# #### GLASSDOOR Reference Link with LOGIN #####
# driver.get('https://www.glassdoor.co.in')
# sleep(2)
# signin = driver.find_element_by_xpath('//*[@id="SiteNav"]/nav/div[2]/div/div/div/button')
# signin.click()
# with_google = driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/button')
# with_google.click()
#
# ### Code for Change Tab and Login and switch tab ####



### Back to Glassdoor ####

# location = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[2]/form/div/div[3]/div/input')
# location.send_keys('United States')
#
# company_name = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[2]/form/div/div[1]/div/div/input')
# company_name.send_keys(CHECK_FOR[1])
# search = driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[4]/div[2]/form/div/button')
# search.click()
#
# glassdoor_target = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/div[1]/article/div/div[1]/div/div[1]/div/div[2]/h2/a').get_attribute('href')
# print(glassdoor_target)
# driver.get(glassdoor_target)
#
#
# sleep(10)
#
#
# #### CRUNCHBASE Reference Link ######
# driver.get('https://www.crunchbase.com')
# search_crunch = driver.find_element_by_xpath('/html/body/chrome/div/app-header/div[1]/multi-search/form/mat-form-field/div/div[1]/div[2]/input')
# search_crunch.send_keys(CHECK_FOR[1]+'\n')
# sleep(2)
# search_place = driver.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[1]/div[1]/mat-accordion/mat-expansion-panel[1]/div/div/div[2]/advanced-filter/filter-identifier-no-suggestions/entity-input/mat-form-field/div/div[1]/div[4]/input')
# search_place.send_keys('Jersey City, NJ')
# sleep(3)
# add_karo = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/mat-option[1]/span/div/div[3]/button')
# add_karo.click()
# sleep(5)
# target_link = driver.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row/grid-cell[2]/div/field-formatter/identifier-formatter/a').get_attribute('href')
# print("Awesome work babe")
# print(target_link)
# driver.get(target_link)
# sleep(5)


#### ASANA Entry Starts #####
driver.get("https://app.asana.com/0/1200584935472213/list")
driver.maximize_window()
gmail=driver.find_element_by_xpath('//*[@id="Login-appRoot"]/div/div[1]/div[2]/div[3]')
gmail.click()
username='//*[@id="identifierId"]'
driver.find_element_by_xpath(username).send_keys(USERNAME+"\n")
# password='//*[@id ="password"]/div[1]/div / div[1]/input'
print("waiting")

sleep(5)
try:
    driver.find_element_by_name('password').send_keys(PASSWORD+"\n")
except:
    print("Takes more time to load")
    sleep(3)
    driver.find_element_by_name('password').send_keys(PASSWORD+"\n")
print("Waiting for the site to load")
sleep(11)

##### SEARCH IF THE COMPANY HISTORY ALREADY EXISTS #######

search_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div/input')
search_box.send_keys(CHECK_FOR[0]+'\n')
hope = 'checking your spelling'
sleep(3)
if hope in driver.page_source:
    print("Success Baby!!!")
else:
    print("Chill")





#### PROCEED FURTHER WITH LOGGING COMPANY DETAILS #######

driver.get('https://app.asana.com/0/1200584935472213/list')
sleep(5)
add_task='//*[@id="asana_main_page"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[1]'
driver.find_element_by_xpath(add_task).click()
print("Clicking done")
new_record='/html/body/div/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[3]/div/div'
# tags_path=driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[5]/div')
# tags_path.click()
pa.typewrite(CHECK_FOR[0],interval=0.1)
sleep(1)
pa.click(1182,352)
pa.typewrite('<500\n',interval=0.5)
pa.typewrite('Internet\n',interval=0.2)
pa.click(794,349)


driver.find_element_by_xpath('//*[@id="highlightedCell"]').click()
print("path is crct")
# sleep(10)
# try:
#     uhm=driver.find_element_by_class_name('BaseTextarea')
#     uhm.click()
#     uhm.send_keys(CHECK_FOR[0])
# except:
#     print("chill pill")
sleep(5)
hmm=driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[3]/div[1]/div/div[2]')
hmm.click()
hmm.send_keys('Almost there ')
print("perfect")

projects = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div[3]/div[2]/div/div/div/div')
projects.click()
project_ip = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div[3]/div[2]/div/div/div/div/input')
project_ip.send_keys('Java')
project_ip.send_keys(Keys.RETURN)
pa.click(1213,451)
pa.typewrite("C#\n")





