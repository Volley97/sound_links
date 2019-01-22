
from selenium import webdriver
import time

driver = webdriver.Chrome('D:\Новая папка\chromedriver.exe')
driver.get('https://www.audioknigi-online.com/after-3.html')
time.sleep(5)
utt = list(map(lambda el:el.get_attribute('src'),driver.find_elements_by_tag_name('audio')))
print(utt)

















