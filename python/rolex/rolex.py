from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.hyundaiwatch.co.kr/contact")

driver.find_element(By.ID, "id")
