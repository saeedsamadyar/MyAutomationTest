from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/saeed/Downloads/chromedriver")
driver.get("https://google.com")
search_field = driver.find_element('name', 'q')



