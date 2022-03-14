import time
import re
import string
import random
from random import choice
from tokenize import String
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions

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

driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(2)
# Create new enquiry menu selection
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[7]/a/p').click()
time.sleep(2)

# New enquiry menu selection
driver.find_element_by_tag_name("button").click()

time.sleep(3)
enquirySelect = driver.find_element_by_xpath('//*[@id="new_enquiry"]/i')
enquirySelect.click()
time.sleep(2)
driver.implicitly_wait(20)
# Enquiry Select salutation path Mr and Mrs
select = Select(driver.find_element_by_id("salutation"))

# select by visible text
select.select_by_visible_text('Mr')
time.sleep(1)
# Enquiry service line input field

# driver.find_element_by_id("first_name").send_keys("Mahbub")
firstName = driver.find_element_by_id("first_name")
firstNameRandom = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(11)])
driver.find_element_by_id("first_name").send_keys(firstNameRandom)
time.sleep(1)

# lastName = driver.find_element_by_id("last_name").send_keys("Alam3")
lastName = driver.find_element_by_id("last_name")
lastNameRandom = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(11)])
driver.find_element_by_id("last_name").send_keys(lastNameRandom)
driver.implicitly_wait(20)
time.sleep(1)

# Date of birth selection


# dobenquirymonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
# dobenquirydays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
# dobenquiryyears  = ['2019','2020','2021']

# dobrandenquiry_date = '{}-{}-{}'.format(*map(choice, [dobenquiryyears, dobenquirymonths, dobenquirydays]))
# # print(rand_date)
# # dob = driver.find_element_by_id('dob').clear()
# dobEnquiry = driver.find_element_by_id('dob').send_keys(dobrandenquiry_date)
# dobEnquiry.perform()
# time.sleep(1)

#Date Of Birth selection
dobEnquiry = driver.find_element_by_id('dob')
driver.execute_script("arguments[0].value = arguments[1]", dobEnquiry, '1/12/2021')
driver.implicitly_wait(20)
time.sleep(0.50)

#Mobile Number selection
mobileNumberDigit = random.randint(10000000000,99999999999)
mobileNumber = driver.find_element_by_id('mobile_primary')
mobileNumber.send_keys(mobileNumberDigit)
driver.implicitly_wait(20)
time.sleep(0.50)

# driver.close()

#Contact Address Section
driver.find_element_by_id("Contact_address_req").send_keys("Dhaka")
time.sleep(1)

# Enquiry Select devision
selectDivision = driver.find_element_by_id('Contact_division_req')
selectDivision.send_keys('Dhaka')
selected_division=driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/ul/li[9]/span')
selected_division.click()
time.sleep(1)




selectDistrict  = driver.find_element_by_id("Contact_district_req")
selectDistrict.send_keys('Dhaka')
selectDistrict.click()
selected_District=driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[15]")
selected_District.click()
# selected_District.click(selectDistrict.click)
time.sleep(1)

selectArea = driver.find_element_by_id('Contact_area_req')
selectArea.send_keys('Savar')
selectArea.click()
selected_Area = driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/ul/li[6]')
selected_Area.click()
# selectArea.click(selectArea)
time.sleep(1)
# selected_Area.click()

selectLocation = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[1]/div[2]/span/div/fieldset/div[2]/div[4]/div/div/input')
selectLocation.send_keys('Mirpur')
time.sleep(0.40)


# identifying the radio button with xpath then click
# driver.find_element_by_css_selector("input[type='radio'][values='postpaid']").click()

select = Select(driver.find_element_by_id('interested_on'))
select.select_by_visible_text('Retail')
time.sleep(0.10)


# Propose Activiton date section

activationmonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
activationdays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
activationyears  = ['2018','2019','2020','2021']
activation_date = '{}-{}-{}'.format(*map(choice, [activationyears, activationmonths, activationdays]))
# print(rand_date)
# dob = driver.find_element_by_id('activation_date').clear()
activationEnquiry = driver.find_element_by_id('activation_date').send_keys(activation_date)
time.sleep(1)

# Source Selection
select = Select(driver.find_element_by_xpath('//*[@id="source"]'))
select.select_by_visible_text('Facebook')
time.sleep(0.10)

# Assign RM selection
assigned_rm = driver.find_element_by_xpath('//*[@id="assigned_rm"]')
assigned_rm.send_keys('Anika Tashin')
assigned_rm.click()
selected_rm = driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[1]/ul/li[67]')
selected_rm.click()
time.sleep(0.50)

# Sales person selection
salesPerson = driver.find_element_by_xpath('//*[@id="sales_person"]')
salesPerson.send_keys('Anika Tashin')
salesPerson.click()
selected_sm = driver.find_element_by_xpath('/html/body/div[13]/div[1]/div[1]/ul/li[66]')
selected_sm.click()
time.sleep(0.50)

# Propose Activiton date section
proposemonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
proposedays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
proposeyears  = ['2021','2022']
propose_date = '{}-{}-{}'.format(*map(choice, [proposeyears, proposemonths, proposedays]))
# print(rand_date)
proposeData = driver.find_element_by_id('proposed_visit_date').clear()
proposeData = driver.find_element_by_id('proposed_visit_date').send_keys(propose_date)
time.sleep(1)


# pvDate = driver.find_element_by_id('proposed_visit_date')
# driver.execute_script("arguments[0].value = arguments[1]", pvDate, '2021-12-18')
# time.sleep(1)



# body = driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(3) > fieldset')
# element = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[3]/fieldset')
# driver.execute_script("arguments[0].scrollIntoView(true);", element)

element = driver.find_element_by_id('show_add_service')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(0.40)



# identifying the radio button with xpath then click
# driver.find_element_by_css_selector("input[type='radio'][values='RM']").click()
# time.sleep(0.50)
# body = driver.find_element_by_css_selector('#show_add_service')
# body.send_keys(Keys.PAGE_DOWN)

# service Modal Open form
show_add_service = driver.find_element_by_id("show_add_service").click()
# show_add_service.click()
time.sleep(0.30)
driver.find_element_by_xpath('//*[@id="service"]').get_attribute('checked')
time.sleep(0.20)

typeSelect = Select(driver.find_element_by_xpath('//*[@id="service_type"]'))
# select by visible text
typeSelect.select_by_visible_text('MiME-TV')
time.sleep(1)

billSelect = driver.find_element_by_xpath('//*[@id="billing_cycle_service"]')
billSelect.send_keys('Monthly')
selected_bill = driver.find_element_by_xpath('//*[@id="billing_cycle_service"]/option[4]').click()
time.sleep(0.20)

packageSelect = driver.find_element_by_xpath('//*[@id="package_service"]')
packageSelect.send_keys('MiME Premium')
selected_Package = driver.find_element_by_xpath('//*[@id="package_service"]/option[13]').click()
time.sleep(1)

#installation adress section
installAddress = driver.find_element_by_id('Installation_address_req')
installAddress.send_keys('Dhaka')

#installation devision section
installDevision  = driver.find_element_by_id('Installation_division_req')
installDevision.send_keys('Dhaka')
installDevision.click()
installed_Devision=driver.find_element_by_xpath('/html/body/div[15]/div[1]/div[1]/ul/li[9]').click()
# installed_Devision.click()
time.sleep(0.30)

#installation District section
installDistrict  = driver.find_element_by_id('Installation_district_req')
installDistrict.send_keys('Dhaka')
installDistrict.click()
installDistrict=driver.find_element_by_xpath('/html/body/div[16]/div[1]/div[1]/ul/li[15]').click()
time.sleep(0.30)

#installation Area section
installArea  = driver.find_element_by_id('Installation_area_req')
installArea.send_keys('Savar')
installArea.click()
installArea=driver.find_element_by_xpath('/html/body/div[17]/div[1]/div[1]/ul/li[6]').click()
time.sleep(0.40)



#installation Location section
installLocation=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/span/span/div/fieldset/div[2]/div[4]/div/div/input')
installLocation.send_keys('Mirpur')
time.sleep(1)

#Service Line Add section
driver.find_element_by_id("add_service").click()
time.sleep(1)

body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)

select = Select(driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[6]/div[1]/fieldset[1]/div[1]/div[1]/span/div/select'))
# select by visible text
select.select_by_visible_text('Connection Fee')
time.sleep(1)
select = Select(driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[6]/div[1]/fieldset[1]/div[1]/div[2]/span/div/select'))
# select by visible text
select.select_by_visible_text('MiME TV')
time.sleep(1)
driver.find_element_by_css_selector("#enquiry-form-validation > div.col-12 > div:nth-child(1) > fieldset.col-8 > div:nth-child(2) > div.col-md-1 > button").click()
time.sleep(1)

# agreed = driver.find_element_by_css_selector("#enquiry-form-validation > div:nth-child(8) > div > div > div.col-2.mt-2 > label > input")
# if agreed.get_attribute("checked") != "true":
#     agreed.click()
# time.sleep(1)

success = driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(8) > div > div > div.save-proceed > button')
# success = driver.find_element_by_id("enquiry_submit").click()
success.submit()
time.sleep(1)

# Create new enquiry menu selection
# followup = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[7]/a/p').click()
# time.sleep(2)

# # New enquiry menu selection
# followup2= driver.find_element_by_tag_name("button").click()
# time.sleep(1)
# # # ---------------------------For Followup page-----------
# body = driver.find_element_by_xpath('body')
# body.send_keys(Keys.PAGE_UP)
# leftbody = driver.find_element_by_xpath('//*[@id="enquiry-left-section"]').perform()

# time.sleep(1)

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(2) > a'))).click()
# time.sleep(1)
# driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel').click()
# time.sleep(1)



# body = driver.find_element_by_xpath('body')
# body = driver.find_element_by_css_selector('body > div.wrapper > div.main-panel.ps.ps--active-y > div.ps__rail-y > div').send_keys(Keys.PAGE_UP                   )
# # body.send_keys(Keys.PAGE_UP)
# time.sleep(0.30)

# # Create new enquiry menu selection
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[7]/a/p').click()
# time.sleep(2)

# # New enquiry menu selection
# driver.find_element_by_tag_name("button").click()
# time.sleep(1)





# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(2) > a'))).click()
# time.sleep(1)
# driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel').click()
# time.sleep(1)


# # ---------------------------For follow up page-----------


# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(2) > a'))).click()
# time.sleep(1)
# driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel').click()
# time.sleep(1)
# followup page


# # # ---------------------------For Followup page-----------

# # time.sleep(0.30)
# # body = driver.find_element_by_css_selector('#horizontalTab > ul > li:nth-child(2) > a')
# # body.send_keys(Keys.PAGE_UP)
# # time.sleep(0.30)
# # body = driver.find_element_by_css_selector('body')
# # body.send_keys(Keys.PAGE_UP)

# # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(2) > a'))).click()
# # time.sleep(1)
# # followupSelect = driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel')
# # followupSelect.click()
# # time.sleep(1)
# comment = driver.find_element_by_id('textAt').send_keys("Close and confirm")
# time.sleep(0.40)

# # identifying the radio button with xpath then click
# # driver.find_element_by_css_selector("input[type='radio'][values='RM']").click()
# # time.sleep(0.50)

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
# # # ---------------------------For Confirm page-----------
# #confirmation tab selection
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#horizontalTab > ul > li:nth-child(3) > a'))).click()
# time.sleep(1)
# confirmSelect = driver.find_element_by_css_selector('#Enquiry > div.card.card-timeline.card-plain > div > ul > li:nth-child(1) > div.timeline-panel')
# confirmSelect.click()
# time.sleep(1)

# # Date of birth selection

# dobmonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
# dobdays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
# dobyears  = ['2021','2022','2023','2024','2025','2026','2027','2028']

# dobrand_date = '{}-{}-{}'.format(*map(choice, [dobyears, dobmonths, dobdays]))
# # print(rand_date)
# dob = driver.find_element_by_id('dob').clear()
# dob = driver.find_element_by_id('dob').send_keys(dobrand_date)
# # driver.execute_script("arguments[0].value = arguments[1]", dob, '1/12/2021')
# time.sleep(1)

# #Nid selection
# nidSelection = driver.find_element_by_id('id_proof')
# nidSelection.send_keys('NID')
# selectNid = driver.find_element_by_xpath('//*[@id="id_proof"]/option[3]')
# selectNid.click()
# time.sleep(0.30)
# #Nid number generation
# # driver.find_element_by_id('id_proof_no').send_keys(3215583315)
# nid = driver.find_element_by_id('id_proof_no')
# nid.send_keys(Keys.CONTROL + "a")
# nid.send_keys(Keys.DELETE)
# nidRandom = ''.join([random.choice(string.ascii_letters
#             + string.digits) for n in range(11)])
# driver.find_element_by_id('id_proof_no').send_keys(nidRandom)

# time.sleep(0.20)
# #browser scroll down
# body = driver.find_element_by_css_selector('body')
# body.send_keys(Keys.PAGE_DOWN)

# #nationality selection
# nationalitySelection = driver.find_element_by_id('nationality')
# nationalitySelection.send_keys('Bangladeshi')
# selectnationality = driver.find_element_by_xpath('//*[@id="nationality"]/option[3]')
# selectnationality.click()
# time.sleep(0.30)
# #AUTO EMAIL Generation
# textEmail= driver.find_element_by_css_selector('#email')
# textEmail.send_keys(Keys.CONTROL + "a")
# textEmail.send_keys(Keys.DELETE)
# time.sleep(0.30)
# #Email generaton random
# def random_char(y):
#     return ''.join(random.choice(string.ascii_letters) for x in range(y))
# driver.find_element_by_id('email').send_keys(random_char(7)+"@gmail.com" )
# time.sleep(0.30)
# driver.find_element_by_id('email').clear()

# # Pay amount selection on selenium
# payAmount = driver.find_element(By.CSS_SELECTOR, "#enquiry-form-validation > div.col-12 > div:nth-child(1) > fieldset.col-4 > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2)").get_attribute("textContent").strip()
# converted_amount = float(payAmount.strip(". BDT").replace(",",""))
# print(converted_amount)
# time.sleep(0.30)
# #browser scroll down
# body = driver.find_element_by_css_selector('body')
# body.send_keys(Keys.PAGE_DOWN)
# driver.find_element_by_css_selector('#enquiry-form-validation > div.col-12 > div:nth-child(1) > fieldset.col-8')
# #browser scroll down
# body = driver.find_element_by_css_selector('body')
# body.send_keys(Keys.PAGE_DOWN)
# #Receive amount input
# total_pay = driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(7) > div > span > form > fieldset > div > div > div:nth-child(1) > div > span > input')
# total_pay.send_keys(Keys.CONTROL + "a")
# total_pay.send_keys(Keys.DELETE)
# total_pay.send_keys(float(converted_amount))
# time.sleep(0.10)
# #Payment mode selection
# select = Select(driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(7) > div > span > form > fieldset > div > div:nth-child(1) > div:nth-child(2) > div > div > span > select'))
# select.select_by_value('cash')
# time.sleep(0.30)


# #Payment receipt section

# receiveBy = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[5]/div/div/span/div/div/input')
# receiveBy.send_keys('Anika Tashin')
# receiveBy.click()
# selected_receive = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/ul/li[51]').click()
# time.sleep(0.30)

# #Book no selection
# driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[1]/div[3]/div/span/input').send_keys(2021)
# time.sleep(0.30)

# driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[1]/div[4]/div/span/input').send_keys(2022)
# time.sleep(0.30)

# # Payment Date  selection

# paymentmonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
# paymentdays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
# paymentyears  = ['2021','2022']
# payment_Date  = '{}-{}-{}'.format(*map(choice, [paymentyears, paymentmonths, paymentdays]))
# paymentDateInput = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[1]/div/span/div/div/div/input').send_keys(payment_Date)
# time.sleep(0.20)
# driver.implicitly_wait(30)


# # service Date  selection

# servicemonths = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
# servicedays   = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
# serviceyears  = ['2021','2022']
# service_Date = '{}-{}-{}'.format(*map(choice, [serviceyears, servicemonths, servicedays]))
# serviceRequiredDate = driver.find_element_by_xpath('//*[@id="enquiry-form-validation"]/div[7]/div/span/form/fieldset/div/div[2]/div/div[3]/div/span/div/div/div/input').send_keys(service_Date)
# time.sleep(1)

# #Confirmation Stage section
# driver.find_element_by_css_selector('#enquiry-form-validation > div:nth-child(8) > div > div > div:nth-child(2) > button').click()
# time.sleep(1)
# print(driver.title)