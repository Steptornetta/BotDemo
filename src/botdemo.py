# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tornetta"
__date__ = "$Jan 25, 2021 1:36:37 PM$"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Hello World")

driver = webdriver.Chrome()
driver.get("http://www.python.org")
time.sleep(5)
driver.close()
