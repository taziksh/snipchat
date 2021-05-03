from seleniumwire import webdriver                                                                                                                                 
from selenium.webdriver.chrome.options import Options                                                                                                          
from selenium.webdriver.support.ui import WebDriverWait
import json
import argparse

parser = argparse.ArgumentParser(description="Args like timeout")

chrome_options = Options()                                                                                                                                     
#chrome_options.add_argument('--headless')
chrome_options.add_argument('user-data-dir=selenium')                                                                                                                      
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.scopes = [
    '.*deezer.*'
]

driver.get('https://www.deezer.com/search/wait%20for%20it%20hamilton')

#RUN THIS ONCE, subsequent runs read from data-dir=selenium
#cookie_btn = WebDriverWait(driver, timeout=10.5).until(lambda arg: arg.find_element_by_class_name('cookie-btn'))
#cookie_btn.click()

try:
    mic_btn = WebDriverWait(driver, timeout=2).until(lambda arg: arg.find_element_by_css_selector('.datagrid-cell>span').click())
except Exception as e:
    pass

for request in driver.requests:
    if request.url.find('https://www.deezer.com/ajax/gw-light.php?method=song.getLyrics') != -1 and request.response:
        body = request.response.body
        print((body))
        print(request.url)
#TODO: <5s by cookie preload and image block

