from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://dzen.ru/')
element = driver.find_element(By.CLASS_NAME, "geoblock__link-aX")
element.click()