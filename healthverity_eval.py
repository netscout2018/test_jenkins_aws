import os
import sys
import re
import requests
import json
import time
import pdb
import subprocess
import gettext
#from tkinter import *
import pymsgbox
import unittest, time, re, pdb
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

#
foundRDS = "FOUND RDS SUBSTRING IN HEADER!!!"
noRDS = "DID NOT FIND RDS SUBSTRING IN HEADER!!!"
foundBkd = "FOUND CYAN BACKGROUND COLOR - rgba 211, 255, 255, 1 !"
noBkd = "CYAN BACKGROUND COLOR MISSING ON SELECTED TABLE ENTRY!!!"
foundBtnandInfo = "FOUND END COMPARE BUTTON AND ROW INFO!!!"
noBtnorInfo = "END COMPARE BUTTON AND/OR ROW INFO MISSING!!!"
#
#colorBK = WritableObject() 
#RDStext = WritableObject() 
#selectedRow = WritableObject() 
#compareB = WritableObject() 
#result = WritableObject()
#count = 0

# class with a write method
class WritableObject:
    def __init__(self):
        self.content = []
    def write(self, string):
        self.content.append(string)


class UntitledTestCase(unittest.TestCase):
		def setUp(self):
#			self.browser = webdriver.Chrome()
			self.browser = webdriver.Chrome(options=options)
#			self.browser = webdriver.Firefox()
			self.browser.implicitly_wait(30)
			self.base_url = "https://ec2instances.info/"
			self.verificationErrors = []
			self.accept_next_alert = True
    
		def test_untitled_test_case(self):
			colorBK = WritableObject() 
			RDStext = WritableObject() 
			selectedRow = WritableObject() 
			compareB = WritableObject() 
			result = WritableObject()
			browser = self.browser
			#pdb.set_trace()
			#browser = webdriver.Chrome()
			browser.maximize_window()
			browser.get(('https://ec2instances.info/'))
			rdstab = browser.find_element_by_css_selector('body > div.page-header > ul > li:nth-child(2) > a')
			rdstab.click()
			element = browser.find_element_by_xpath('/html/body/div[1]/h1')
			RDStext = element.text
			assert RDStext == 'EC2Instances.info Easy Amazon RDS Instance Comparison'
			# Check color attribute of a row when selected
			element = browser.find_element_by_xpath("//*[@id='db.t2.small']/td[1]")
			bkclr = browser.find_element_by_id('db.t2.small')
			element.click()
			time.sleep(3)
			bkclr = browser.find_element_by_id('db.t2.small')
			colorBK = bkclr.value_of_css_property('background-color')
			time.sleep(3)
#			assert colorBK == "rgb(211, 255, 255)"
			comparebtn = browser.find_element_by_xpath("//*[@id='menu']/div/button[1]")
			comparebtn.click()
			time.sleep(2)
			rowvisible = browser.find_element_by_xpath("//*[@id='db.t2.small']/td[1]")
			selectedRow = rowvisible.text
			compareB = comparebtn.text
			assert comparebtn.text == "End Compare"
			browser.close()

		def is_element_present(self, how, what):
			try: self.browser.find_element(by=how, value=what)
			except NoSuchElementException as e: return False
			return True
    
		def is_alert_present(self):
			try: self.browser.switch_to_alert()
			except NoAlertPresentException as e: return False
			return True
    
		def close_alert_and_get_its_text(self):
			try:
				alert = self.browser.switch_to_alert()
				alert_text = alert.text
				if self.accept_next_alert:
					alert.accept()
				else:
					alert.dismiss()
				return alert_text
			finally: self.accept_next_alert = True
    
		def tearDown(self):
			self.browser.quit()
			#self.browser.close()
			self.assertEqual([], self.verificationErrors)

			#pdb.set_trace()

if __name__ == "__main__":
	unittest.main()
