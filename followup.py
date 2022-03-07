import time
import re
import random
import string
from random import choice
from tokenize import String
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# from google-chrome loading
driver = webdriver.Chrome(
    executable_path="E:\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")

# from login page url
driver.get("https://testconnect.mimebd.com/login")
time.sleep(2)
# User-name-and-password-input-field
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("@Test2021")
driver.find_element_by_tag_name("button").submit()
#FOR Maximize window
driver.maximize_window()
time.sleep(2)
# Create new enquiry menu selection
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[7]/a/p').click()
time.sleep(2)

# New enquiry menu selection
driver.find_element_by_tag_name("button").click()
time.sleep(1)
# # # ---------------------------For Followup page-----------
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(2) > a'))).click()
time.sleep(1)
driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel').click()
# driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(2) > div.timeline-panel.active-class').click()
time.sleep(1)




# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li.col-md-3.active.followup-color > a'))).click()
# time.sleep(1)
# followupSelect = driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel > div.timeline-heading > span')
# followupSelect.click()
# time.sleep(1)
comment = driver.find_element_by_id('textAt').send_keys("Close and confirm")
time.sleep(0.40)

# #identifying the radio button with xpath then click
driver.find_element_by_css_selector("input[type='radio'][values='RM']").click()
time.sleep(0.50)



# department = Select(driver.find_element_by_xpath('//*[@id="followup-discussion-section"]/span/div[2]/div[3]/div/div/span/select'))
# department.select_by_value('4')
# time.sleep(1)

# assignRM = Select(driver.find_element_by_xpath('//*[@id="followup-discussion-section"]/span/div[2]/div[4]/div/div/span/select'))
# assignRM.select_by_value('40')
# time.sleep(1)

# select = Select(driver.find_element_by_xpath('//*[@id="followup-discussion-section"]/span/div[2]/div[5]/div/div/span/select'))
# select.select_by_value('4')
# time.sleep(1)

# driver.find_element_by_css_selector('#followup-discussion-section > span > div.card-body.p-0 > div:nth-child(6) > div.col-md-8 > button').click()
# time.sleep(1)
# # ---------------------------For Confirm page-----------
#confirmation tab selection
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(3) > a'))).click()
time.sleep(1)
confirmSelect = driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(5) > div.timeline-panel')
confirmSelect.click()
time.sleep(1)

# Date of birth selection

dobmonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
dobdays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
dobyears  = ['2021','2022','2023','2024','2025','2026','2027','2028']

dobrand_date = '{}-{}-{}'.format(*map(choice, [dobyears, dobmonths, dobdays]))
# print(rand_date)
dob = driver.find_element_by_id('dob').clear()
dob = driver.find_element_by_id('dob').send_keys(dobrand_date)
# driver.execute_script("arguments[0].value = arguments[1]", dob, '1/12/2021')
time.sleep(1)

#Nid selection
nidSelection = driver.find_element_by_id('id_proof')
nidSelection.send_keys('NID')
selectNid = driver.find_element_by_xpath('//*[@id="id_proof"]/option[3]')
selectNid.click()
time.sleep(0.30)
#Nid number generation
# driver.find_element_by_id('id_proof_no').send_keys(3215583315)
nid = driver.find_element_by_id('id_proof_no')
nid.send_keys(Keys.CONTROL + "a")
nid.send_keys(Keys.DELETE)
nidRandom = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(11)])
driver.find_element_by_id('id_proof_no').send_keys(nidRandom)

time.sleep(0.20)
#browser scroll down
body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)

#nationality selection
nationalitySelection = driver.find_element_by_id('nationality')
nationalitySelection.send_keys('Bangladeshi')
selectnationality = driver.find_element_by_xpath('//*[@id="nationality"]/option[3]')
selectnationality.click()
time.sleep(0.30)
#AUTO EMAIL Generation
textEmail= driver.find_element_by_css_selector('#email')
textEmail.send_keys(Keys.CONTROL + "a")
textEmail.send_keys(Keys.DELETE)
time.sleep(0.30)
#Email generaton random
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
driver.find_element_by_id('email').send_keys(random_char(7)+"@gmail.com" )
time.sleep(0.30)
driver.find_element_by_id('email').clear()

# Pay amount selection on selenium
payAmount = driver.find_element(By.CSS_SELECTOR, "#enquiry-form-validation > div.col-12 > div:nth-child(1) > fieldset.col-4 > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2)").get_attribute("textContent").strip()
converted_amount = float(payAmount.strip(". BDT").replace(",",""))
print(converted_amount)
time.sleep(0.30)
#browser scroll down
body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)
driver.find_element_by_css_selector('#enquiry-form-validation > div.col-12 > div:nth-child(1) > fieldset.col-8')
#browser scroll down
body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)
#Receive amount input
total_pay = driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(7) > div > span > form > fieldset > div > div > div:nth-child(1) > div > span > input')
total_pay.send_keys(Keys.CONTROL + "a")
total_pay.send_keys(Keys.DELETE)
total_pay.send_keys(float(converted_amount))
time.sleep(0.10)
#Payment mode selection
select = Select(driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(7) > div > span > form > fieldset > div > div:nth-child(1) > div:nth-child(2) > div > div > span > select'))
select.select_by_value('cash')
time.sleep(0.30)


#Payment receipt section

receiveBy = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[5]/div/div/span/div/div/input')
receiveBy.send_keys('Anika Tashin')
receiveBy.click()
selected_receive = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/ul/li[51]').click()
time.sleep(0.30)

#Book no selection
driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[1]/div[3]/div/span/input').send_keys(2021)
time.sleep(0.30)

driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[1]/div[4]/div/span/input').send_keys(2022)
time.sleep(0.30)

# Payment Date  selection

paymentmonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
paymentdays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
paymentyears  = ['2021','2022']
payment_Date  = '{}-{}-{}'.format(*map(choice, [paymentyears, paymentmonths, paymentdays]))
paymentDateInput = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[1]/div/span/div/div/div/input').send_keys(payment_Date)
time.sleep(0.20)
driver.implicitly_wait(30)


# service Date  selection

servicemonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
servicedays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
serviceyears  = ['2021','2022']
service_Date = '{}-{}-{}'.format(*map(choice, [serviceyears, servicemonths, servicedays]))
serviceRequiredDate = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[3]/div/span/div/div/div/input').send_keys(service_Date)
time.sleep(1)

#Confirmation Stage section
driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(8) > div > div > div:nth-child(2) > button').click()
time.sleep(1)
print(driver.title)
# driver.close()
