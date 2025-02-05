import pandas as pd
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 


service = webdriver.ChromeService(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.ambitionbox.com/list-of-companies?page=1")

action = ActionChains(driver) 
action.pause(5000)