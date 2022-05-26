from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PATH = 'msedgedriver.exe'
driver = webdriver.Edge(PATH)

driver.get('https://members.whistlebear.ca/TeeTimes/TeeSheet.aspx')

driver.find_element(by=By.ID, value='p_lt_page_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_UserName').send_keys('kmelv41')
driver.find_element(by=By.ID, value='p_lt_page_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_Password').send_keys('K910623m')
driver.find_element(by=By.ID, value='p_lt_page_content_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_Password').send_keys(Keys.RETURN)

time.sleep(20)

participants = driver.find_elements(by=By.CLASS_NAME, value="CMSMenuItem")

print(participants)

# driver.findElement(By.xpath('/html/body')).sendKeys('kmelv41')



'''
url = r'https://members.whistlebear.ca/TeeTimes/TeeSheet.aspx'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
print(doc.prettify())
'''