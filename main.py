
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#driver = webdriver.Chrome(executable_path="/Users/saeed/Downloads/chromedriver")
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())

driver.get("http://google.com")
sleep(2)
driver.find_element('name', 'q').send_keys("Wikipedia")
sleep(3)
driver.quit()
#search_field = driver.find_element('name', 'q')



