#coding = utf-8  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

  
driver = webdriver.Firefox()
driver.get('http://www.python.org')
time.sleep(3)
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()